from dotenv import load_dotenv
from langsmith import Client

load_dotenv()

client = Client()
dataset_name = "University Fee Policy Dataset"

try:
    dataset = client.create_dataset(
        dataset_name=dataset_name,
        description="Evaluation dataset for University Fee Policy Assistant"
    )
except Exception:
    datasets = list(client.list_datasets(dataset_name=dataset_name))
    dataset = datasets[0]

examples = [
    {
        "inputs": {"question": "What is the late fee for exam registration?"},
        "outputs": {
            "expected_answer": "Students must pay a late fee of ₹500 if exam registration is completed after the deadline."
        }
    },
    {
        "inputs": {"question": "When will hall tickets be generated?"},
        "outputs": {
            "expected_answer": "Hall tickets are generated only after successful payment of exam fees."
        }
    },
    {
        "inputs": {"question": "Can students get exam fee refund?"},
        "outputs": {
            "expected_answer": "Hall tickets are generated only after successful payment of exam fees."
        }
    },
    {
        "inputs": {"question": "What is the affiliation fee rule?"},
        "outputs": {
            "expected_answer": "Colleges must clear affiliation fees before semester approval."
        }
    },

    # Out-of-domain questions
    {
        "inputs": {"question": "How is the health of Trump?"},
        "outputs": {
            "expected_answer": "I don't know from the given policy."
        }
    },
    {
        "inputs": {"question": "Who won the IPL final?"},
        "outputs": {
            "expected_answer": "I don't know from the given policy."
        }
    },
    {
        "inputs": {"question": "What is the capital of Japan?"},
        "outputs": {
            "expected_answer": "I don't know from the given policy."
        }
    },
    {
        "inputs": {"question": "Explain machine learning."},
        "outputs": {
            "expected_answer": "I don't know from the given policy."
        }
    }
]

for example in examples:
    client.create_example(
        inputs=example["inputs"],
        outputs=example["outputs"],
        dataset_id=dataset.id
    )

print("Dataset created/updated successfully:", dataset_name)