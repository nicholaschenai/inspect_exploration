from typing import Any

from inspect_ai import Task, task, eval
from inspect_ai.solver import generate, solver, chain, Solver, Generate, TaskState
from inspect_ai.dataset import json_dataset
from inspect_ai.scorer import pattern

from prompt_generator import PromptGenerator

from utils import record_to_sample

model_name = "openai/gpt-4o-mini-2024-07-18"


# COT_PROMPT="""
# {prompt}

# Before answering the question, think step by step.
# """

base_prompt_generator = PromptGenerator.create("zeroshot")
cot_prompt_generator = PromptGenerator.create("zeroshot-cot")

pattern_str = r"<answer>(.*)</answer>"

@task
def morehopqa() -> Task:
    """Inspect task implementing the morehopqa benchmark."""
    dataset = json_dataset(
        json_file="data/morehopqa_final_150samples.json",
        sample_fields=record_to_sample,
        limit=5
    )

    return Task(
        dataset=dataset,
        scorer=pattern(pattern_str)
    )

@solver
def prompt_solver(cot: bool=False, **params: Any) -> Solver:
    prompt_gen = cot_prompt_generator if cot else base_prompt_generator

    async def solve(state: TaskState, generate: Generate) -> TaskState:
        prompt = state.user_prompt
        metadata = state.metadata
        prompt.text = prompt_gen.get_prompt('', metadata['context'], prompt.text)
        return state

    return solve

@solver
def final_solver(cot: bool=False):
    return chain(
        prompt_solver(cot=cot), 
        generate(cache=True)
    )



if __name__ == "__main__":
    eval(morehopqa(), model=model_name, solver=final_solver(cot=False))
    eval(morehopqa(), model=model_name, solver=final_solver(cot=True))




