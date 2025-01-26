
## Project Structure
- `main.py`: Entry point containing task definition, solver implementation, and evaluation setup
- `utils.py`: Utility functions for data processing and converting to Sample objects for Inspect
- `prompt_generator.py`: Prompt generation logic from MorehopQA dataset for zero-shot with and without CoT
- `data/`: Contains the MorehopQA dataset samples
  - `morehopqa_final_150samples.json`: 150 sample subset of MorehopQA dataset

## Components

### Task Definition
The project implements the MorehopQA benchmark as an Inspect task, with pattern-based (regex) answer scoring by extracting from `<answer>` tags (as in the MorehopQA dataset)

### Prompt Generation
Two prompt generation strategies are implemented:
1. Zero-shot: Direct question answering
2. Zero-shot with CoT: Includes "Let's think step by step" instruction

We include the context in the prompt, as in the MorehopQA dataset.

### Solver Pipeline
The solver chain consists of:
1. Prompt preparation with context integration
2. Model generation with caching

## Usage
```bash
python main.py
```

Should generate logs in the `logs` directory which can be viewed with
```bash
inspect view
```

or via VSCode extension
