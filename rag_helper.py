from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader
from langchain_community.llms import Ollama

def run_rag(query, pdf_path):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(docs)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.from_documents(split_docs, embeddings)
    retriever = db.as_retriever()
    llm = Ollama(model="tinyllama")
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return chain.run(query)
