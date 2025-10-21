# AI RAG Chatbot 🌐

Bu proje, **AI, ML, Deep Learning** konularında soruları yanıtlayabilen bir **Retrieval-Augmented Generation (RAG) Chatbot** içerir.  
Projede hem **Streamlit web uygulaması** hem de **Jupyter Notebook** bulunur.

> ⚠️ Not: Bu proje **rag_env** adındaki Python sanal ortamında çalıştırılmıştır.  
> Lütfen ortamı aktif ederek ve gerekli kütüphaneleri yükleyerek çalıştırın.

---

## 🚀 Özellikler

- Wikipedia AI Glossary veri setinden embedding çıkarma
- Sentence-Transformers ile metin embedding’leri
- ChromaDB vector store ile hızlı doküman arama
- Google Flan-T5 küçük modelini kullanarak cevap üretimi
- Streamlit arayüzü ile kolay kullanım
- Batch embedding ile büyük veri setlerinde kernel çökmesini önler

---

## 🛠️ Kurulum

1. Rag_env ortamını aktif et:
source ~/rag_env/bin/activate



2. Gerekli kütüphaneleri yükle.
pip install -r requirements.txt

Örnek requirements.txt içeriği:
streamlit
sentence-transformers
chromadb
transformers
torch
pandas


3. Streamlit uygulamasını çalıştır:
streamlit run app.py

4. Jupyter Notebook’u çalıştırmak için:
jupyter notebook
Notebook kernel’i rag_env olmalı.


📁 Dosya Yapısı
akbank3/
│
├─ app.py               # Streamlit uygulaması
├─ akbank.ipynb         # Notebook
├─ data/
│   └─ Wikipedia_AI_Glossary.csv
└─ README.md
