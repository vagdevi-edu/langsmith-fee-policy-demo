from dotenv import load_dotenv
from langsmith import evaluate
from app import ask_assistant

load_dotenv()

DATASET_NAME = "University Fee Policy Dataset"


def target(inputs: dict):
    result = ask_assistant(inputs["question"])
    return {"answer": result["answer"]}


def domain_safety_evaluator(outputs: dict, reference_outputs: dict):
    actual = outputs.get("answer", "").lower().strip()
    expected = reference_outputs.get("expected_answer", "").lower().strip()

    if "i don't know from the given policy" in expected:
        passed = "i don't know" in actual
    else:
        passed = expected in actual

    return {
        "key": "domain_safety",
        "score": 1 if passed else 0,
        "comment": f"Expected: {expected} | Actual: {actual}"
    }


evaluate(
    target,
    data=DATASET_NAME,
    evaluators=[domain_safety_evaluator],
    experiment_prefix="manager-demo-domain-safety"
)

print("Evaluation completed.")