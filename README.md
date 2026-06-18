# LangSmith AI Observability Demo

A professional demonstration of LangSmith capabilities using a University Fee Policy Assistant built with Python and Streamlit.

This project showcases how LangSmith can be used for:

* Tracing
* Monitoring
* Evaluation
* Dataset Management
* Failure Analysis
* AI Application Observability

---

# Project Overview

The application acts as a University Fee Policy Assistant that answers questions based on predefined university policy documents.

Users can:

* Ask policy-related questions
* View retrieved policy documents
* See generated answers
* Explore LangSmith traces
* Run evaluations against datasets

The project demonstrates how LangSmith helps developers build reliable AI systems.

---

# Architecture

```text
User Question
      │
      ▼
Policy Retriever
      │
      ▼
Relevant Policy Document
      │
      ▼
Answer Generator
      │
      ▼
Final Response
      │
      ▼
LangSmith Trace
```

---

# LangSmith Features Demonstrated

## Tracing

Every execution is recorded in LangSmith.

Example:

```text
University Fee Policy Assistant
├── Retrieve Relevant Policy
├── Generate Final Answer
└── Return Response
```

Captured information:

* Input question
* Retrieved document
* Generated answer
* Execution duration
* Run status

---

## Monitoring

Monitoring tracks application health.

Metrics include:

* Success Rate
* Latency
* Total Runs
* Error Count
* Execution Status

Important:

Monitoring checks whether the application executed successfully.

It does **not** determine whether the answer is correct.

---

## Dataset Management

A LangSmith dataset named:

```text
University Fee Policy Dataset
```

contains:

### In-Domain Questions

* What is the late fee for exam registration?
* When will hall tickets be generated?
* Can students get exam fee refund?
* What is the affiliation fee rule?

### Out-of-Domain Questions

* How is the health of Trump?
* Who won the IPL final?
* What is the capital of Japan?
* Explain machine learning?

---

## Evaluation

Custom evaluators are used to measure answer quality.

Example:

Question:

```text
How is the health of Trump?
```

Expected:

```text
I don't know from the given policy.
```

Actual:

```text
Based on university policy: Students must pay a late fee of ₹500...
```

Result:

```text
FAILED
Score = 0
```

This demonstrates how LangSmith identifies semantic failures.

---

## Failure Analysis

The project intentionally includes out-of-domain questions to demonstrate evaluation failures.

Example:

```text
Question:
How is the health of Trump?
```

The application executes successfully.

Monitoring:

```text
SUCCESS
```

Evaluation:

```text
FAILED
```

This illustrates the difference between technical success and answer correctness.

---

# Tech Stack

* Python 3.12
* Streamlit
* LangSmith
* Python Dotenv

---

# Project Structure

```text
langsmith-fee-policy-demo/
│
├── app.py
├── ui.py
├── policy_docs.py
├── create_dataset.py
├── evaluate_app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/vagdevi-edu/langsmith-fee-policy-demo.git
cd langsmith-fee-policy-demo
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=university-fee-policy-demo
```

---

# Running the Application

Start the Streamlit UI:

```bash
streamlit run ui.py
```

Open:

```text
http://localhost:8501
```

---

# Creating Dataset

```bash
python create_dataset.py
```

---

# Running Evaluation

```bash
python evaluate_app.py
```

Evaluation results can be viewed directly in LangSmith Experiments.

---

# Key Learnings

This project demonstrates:

* AI Observability
* End-to-End Tracing
* Monitoring vs Evaluation
* Dataset-Based Testing
* Failure Detection
* RAG-Style Workflow Analysis

---

# Author

**Vagdevi Malineni**

AI / ML Enthusiast | Python Developer | LLM & Observability Explorer
