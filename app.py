import streamlit as st
from planner_agent import query_fin_agent
from rag_helper import run_rag
import os

st.set_page_config(page_title="FinAgent AI", layout="wide")
st.title("🏦 FinAgent AI – Smart BFSI Assistant with RAG + Agent")

st.sidebar.header("📂 Upload BFSI Documents")
docs = st.sidebar.file_uploader("Upload PDFs (policy, terms, statements)", type=["pdf"], accept_multiple_files=True)

if docs:
    with open("temp_combined.pdf", "wb") as f:
        for d in docs:
            f.write(d.read())
    st.success("📄 PDFs combined and ready for RAG!")

st.divider()
st.subheader("🤖 Ask FinAgent (LLM)")
user_prompt = st.text_input("Ask a BFSI question (e.g., What is term insurance?)")
if user_prompt:
    response = query_fin_agent(user_prompt)
    st.markdown(response)

st.divider()
st.subheader("📚 Ask About Uploaded PDFs (RAG)")
rag_prompt = st.text_input("Ask a doc-specific question (e.g., What is the premium term?)")
if rag_prompt:
    answer = run_rag(rag_prompt, "temp_combined.pdf")
    st.markdown(answer)
