import streamlit as st
from app import ask_assistant

st.set_page_config(
    page_title="LangSmith AI Observability Demo",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #f8fafc;
}

h1, h2, h3, h4, h5, h6, p, label {
    color: black;
}

.hero {
    padding: 30px;
    border-radius: 18px;
    background: linear-gradient(135deg, #0f172a, #1e3a8a);
    color: white;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 38px;
    margin-bottom: 8px;
    color: white;
}

.hero p {
    color: white;
    font-size: 17px;
}

.metric-card {
    padding: 20px;
    border-radius: 14px;
    background-color: #eef2ff;
    border-left: 5px solid #2563eb;
    color: black;
    min-height: 135px;
}

.metric-card h3 {
    color: black;
}

.metric-card p {
    color: black;
}

.card {
    padding: 22px;
    border-radius: 16px;
    background-color: white;
    border: 1px solid #e5e7eb;
    box-shadow: 0px 4px 14px rgba(0,0,0,0.06);
    margin-bottom: 18px;
    color: black;
}

.card h4, .card p {
    color: black;
}

.answer-box {
    padding: 22px;
    border-radius: 14px;
    background-color: #ecfdf5;
    border-left: 6px solid #16a34a;
    font-size: 18px;
    color: black;
}

.warning-box {
    padding: 22px;
    border-radius: 14px;
    background-color: #fff7ed;
    border-left: 6px solid #f97316;
    color: black;
    font-size: 18px;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #1e40af, #2563eb);
    color: white !important;
    border-radius: 12px;
    border: none;
    height: 50px;
    font-size: 18px;
    font-weight: 600;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #1d4ed8, #3b82f6);
    color: white !important;
}

.stTextInput label, .stSelectbox label {
    color: black !important;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🧠 LangSmith AI Observability Demo</h1>
    <p>University Fee Policy Assistant with Tracing, Monitoring, Datasets, and Evaluation</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h3>🔍 Tracing</h3>
        <p>Tracks every step of the AI workflow.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h3>📡 Monitoring</h3>
        <p>Tracks run status, latency, and failures.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h3>📊 Evaluation</h3>
        <p>Checks answer correctness using datasets.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("### Ask the University Policy Assistant")

question = st.text_input(
    "Enter your question",
    value="What is the late fee for exam registration?"
)

sample_questions = [
    "What is the late fee for exam registration?",
    "When will hall tickets be generated?",
    "Can students get exam fee refund?",
    "What is the affiliation fee rule?",
    "What is the hostel fee?"
]

selected = st.selectbox("Or choose a sample question", sample_questions)

if st.button("🚀 Run AI Assistant"):
    final_question = question if question.strip() else selected

    with st.spinner("Running assistant and sending trace to LangSmith..."):
        result = ask_assistant(final_question)

    st.success(result["answer"])
    
    st.markdown(
    """
    <h2 style='color:White; margin-top:25px;'>
        📋 AI Assistant Response
    </h2>
    """,
    unsafe_allow_html=True
)

    left, right = st.columns([2, 1])

    with left:
        st.markdown("### ✅ Final Answer")

        if "don't know" in result["answer"].lower():
            st.markdown(
                f"""
                <div class="warning-box">
                    <b>{result["answer"]}</b>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div class="answer-box">
                    <b>{result["answer"]}</b>
                </div>
                """,
                unsafe_allow_html=True
            )

    with right:
        st.markdown("### 📌 Query")
        st.info(result["question"])

    st.markdown("### 📚 Retrieved Policy Documents")

    if result["retrieved_docs"]:
        for doc in result["retrieved_docs"]:
            st.markdown(
                f"""
                <div class="card">
                    <h4>{doc['title']}</h4>
                    <p>{doc['content']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.warning("No relevant policy document found.")

    st.markdown("### 🧭 LangSmith Trace Flow")

    st.code("""
University Fee Policy Assistant
├── Retrieve Relevant Policy
├── Generate Final Answer
└── Return Response
""")

    st.markdown("### 🔗 Open LangSmith Dashboard")

    st.write(
        "Open LangSmith to view traces, inputs, outputs, retrieved documents, latency, and run status."
    )

    st.link_button(
        "Open LangSmith Dashboard",
        "https://smith.langchain.com/"
    )