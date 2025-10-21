import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
from transformers import pipeline

# -------------------------------
# 1️⃣ Dataset
# -------------------------------
df = pd.read_csv('./data/Wikipedia_AI_Glossary.csv')
df = df.dropna(subset=["Title", "Wikipedia_page_description"])
df["Wikipedia_page_description"] = df["Wikipedia_page_description"].apply(lambda x: x.replace("\n", " ").strip())
texts = df["Wikipedia_page_description"].tolist()

st.title("AI RAG Chatbot 🌐")
st.write("Ask questions about AI, ML, Deep Learning, or related topics.")

# -------------------------------
# 2️⃣ Embeddings
# -------------------------------
@st.cache_data
def get_embeddings(texts):
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = embedder.encode(texts, show_progress_bar=True)
    return embedder, embeddings

embedder, embeddings = get_embeddings(texts)

# -------------------------------
# 3️⃣ Chroma Vector Store
# -------------------------------
@st.cache_resource
def create_vector_store(texts, embeddings):
    client = chromadb.Client(Settings(anonymized_telemetry=False))
    # Eğer koleksiyon varsa sil
    if "ai_glossary" in [c.name for c in client.list_collections()]:
        client.delete_collection("ai_glossary")
    collection = client.create_collection("ai_glossary")
    for i, (text, emb) in enumerate(zip(texts, embeddings)):
        collection.add(documents=[text], embeddings=[emb.tolist()], ids=[str(i)])
    return collection

collection = create_vector_store(texts, embeddings)

# -------------------------------
# 4️⃣ QA Model (Tiny Flan-T5)
# -------------------------------
@st.cache_resource
def load_qa_model():
    return pipeline("text2text-generation", model="google/flan-t5-small", tokenizer="google/flan-t5-small")

qa_model = load_qa_model()

# -------------------------------
# 5️⃣ RAG Query
# -------------------------------
def rag_query(question, top_k=3):
    query_vec = embedder.encode([question])
    results = collection.query(query_embeddings=query_vec.tolist(), n_results=top_k)
    top_docs = results["documents"][0]

    # Contexti birleştir ve token sınırlaması (~300 token)
    context = " ".join(top_docs)
    context = context[:3000]  # Daha uzun context

    prompt = f"""
You are an AI expert. Answer the question using the following context.
Provide a detailed explanation in 3-5 sentences.

Context: {context}

Question: {question}
Answer:
"""
    answer = qa_model(prompt, max_new_tokens=600, do_sample=True, temperature=0.7)[0]["generated_text"]
    return answer.strip()

# -------------------------------
# 6️⃣ Streamlit UI
# -------------------------------
user_input = st.text_input("Your question:")
if user_input:
    with st.spinner("Generating answer..."):
        answer = rag_query(user_input)
    st.success(answer)
