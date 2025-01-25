from typing import Any

from inspect_ai.dataset import Sample

def record_to_sample(record: dict[str, Any]) -> Sample:
    """
    Convert a record from the morehopqa dataset to a Sample object.
    """
    return Sample(
        input=record["question"],
        target=record["answer"],
        metadata={
            "context": record["context"],
            "previous_question": record["previous_question"],
            "previous_answer": record["previous_answer"],
            "question_decomposition": record["question_decomposition"],
            # "question_on_last_hop": record["question_on_last_hop"],
            "question_on_last_hop": record["ques_on_last_hop"],
            "answer_type": record["answer_type"],
            "previous_answer_type": record["previous_answer_type"],
            "no_of_hops": record["no_of_hops"],
            "reasoning_type": record["reasoning_type"],
            "pattern": record["pattern"],
            "subquestion_patterns": record["subquestion_patterns"],
            "cutted_question": record["cutted_question"]
        }
    )


# note: for HF (which cant seem to work), question_on_last_hop is as-is, but for json, it is ques_on_last_hop

# dataset = hf_dataset(
#     path="alabnii/morehopqa",
#     split="test",
#     sample_fields=record_to_sample,
#     trust=True,
#     limit=5,
#     download_mode="force_redownload",
#     data_files={"test": "verified/*.parquet"},
#     data_dir="verified",
#     streaming=False,
#     cached=False
# )