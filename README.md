# JE25-FinAgent-AI
Gen Ai

🏦💡 FinAgent AI – BFSI Smart Assistant with RAG and AI Agents
📌 Overview
FinAgent AI is an intelligent assistant for the BFSI sector that:

Answers customer queries on banking, finance, and insurance using RAG from uploaded PDFs

Uses an AI planning agent (via Ollama) to draft financial advice, policy summaries, or investment explanations

Supports multi-doc PDF Q&A, summary generation, and personalized recommendations

🔍 Key Features
Feature	Description
📂 PDF Upload + RAG	Upload policy documents, statements, or financial guides and ask questions
🤖 AI Financial Planner Agent	Ask financial questions (e.g., “Best saving option for 5 years?”)
📊 Personalized Summary Generator	Auto-generates executive summaries from uploaded BFSI documents
📝 Compliance & Risk Explanation	Extracts and explains regulatory sections from documents
🔐 Private & Offline (Ollama LLM)	All processing is done locally, privacy-first

📘 README.md
markdown
Copy
Edit
# 🏦 FinAgent AI – Smart BFSI Assistant with RAG + Agents

FinAgent AI helps users understand financial and insurance documents using RAG-based Q&A and agent-based reasoning.

## 💡 Features
- Upload PDFs like insurance policies or savings plans
- Ask general or document-specific questions
- Get investment summaries and compliance insights

## 🚀 How to Run

1. Clone the repo:
```bash
git clone https://github.com/yourusername/FinAgent-AI
cd FinAgent-AI
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Start Ollama and pull LLM:

bash
Copy
Edit
ollama serve
ollama pull tinyllama
Run the app:

bash
Copy
Edit
streamlit run app.py
Upload a PDF → Ask your questions → Get instant BFSI insights!
