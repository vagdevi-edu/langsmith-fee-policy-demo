import time
from dotenv import load_dotenv
from langsmith import traceable
from policy_docs import POLICY_DOCS

load_dotenv()

STOPWORDS = {
    "what", "is", "the", "for", "when", "will", "be", "can",
    "students", "get", "rule", "of", "a", "an", "after", "fee"
}


@traceable(name="Retrieve Relevant Policy")
def retrieve_policy(question: str):
    question_words = [
        word.strip("?.!,").lower()
        for word in question.split()
        if len(word.strip("?.!,")) > 3
    ]

    best_doc = None
    best_score = 0

    for doc in POLICY_DOCS:
        text = f"{doc['title']} {doc['content']}".lower()

        score = 0
        for word in question_words:
            if word in text:
                score += 1

        if score > best_score:
            best_score = score
            best_doc = doc

    if best_score == 0:
        return []

    return [best_doc]

@traceable(name="Generate Final Answer")
def generate_answer(question: str, context_docs):
    if not context_docs:
        return "I don't know from the given policy."

    return f"Based on university policy: {context_docs[0]['content']}"

@traceable(name="University Fee Policy Assistant")
def ask_assistant(question: str):
    context_docs = retrieve_policy(question)
    answer = generate_answer(question, context_docs)

    return {
        "question": question,
        "retrieved_docs": context_docs,
        "answer": answer,
    }


if __name__ == "__main__":
    questions = [
        "What is the late fee for exam registration?",
        "When will hall tickets be generated?",
        "Can students get exam fee refund?",
        "What is the affiliation fee rule?",
        "What is the hostel fee?",
    ]

    for q in questions:
        result = ask_assistant(q)

        print("\nQuestion:", result["question"])
        print("Retrieved Docs:", result["retrieved_docs"])
        print("Answer:", result["answer"])

    time.sleep(3)