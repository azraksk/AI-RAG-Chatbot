# AI RAG Chatbot 🌐

Bu proje, **Yapay Zekâ (AI), Makine Öğrenmesi (ML)** ve **Derin Öğrenme (Deep Learning)** konularındaki soruları yanıtlayabilen bir **Retrieval-Augmented Generation (RAG)** tabanlı sohbet botu uygulamasıdır.  
Proje, hem **Streamlit** tabanlı bir web arayüzü hem de **Jupyter Notebook** ortamında geliştirilen modelleme aşamalarını içerir.

> ⚠️ Not: Proje, `rag_env` adlı Python sanal ortamında geliştirilmiştir. Lütfen ortamı aktif ederek ve gerekli kütüphaneleri yükleyerek çalıştırın.

---

## 🎯 Projenin Amacı

Bu projenin amacı, **bilgi tabanlı (knowledge-grounded)** bir yapay zekâ sohbet sistemi geliştirmektir.  
Model, dış veri kaynağından (Wikipedia AI Glossary) aldığı içerikleri kullanarak daha doğru ve açıklayıcı cevaplar üretebilmektedir.  
Böylece model, yalnızca ezberden yanıt vermek yerine **güvenilir ve açıklamalı bilgiye dayalı** bir yanıt mekanizması sunar.

---

## 📊 Veri Seti Hakkında

Proje, **Wikipedia AI Glossary** veri setini kullanır.  
Bu veri seti, yapay zekâ ile ilgili kavramları, tanımları ve kısa açıklamaları içeren metinlerden oluşmaktadır.  
Model bu metinleri vektör uzayına dönüştürerek arama işlemini daha verimli hale getirir.

---

## 🧠 Kullanılan Yöntemler

- **Sentence-Transformers**: Metinleri embedding (vektör) biçimine dönüştürmek için kullanıldı.  
- **ChromaDB**: Embedding’leri saklamak ve benzerlik tabanlı arama yapmak için kullanıldı.  
- **Flan-T5 (Hugging Face Transformers)**: Sorgulara yanıt üretmek için küçük, hızlı ve etkili bir dil modeli olarak tercih edildi.  
- **Streamlit**: Kullanıcıların tarayıcı üzerinden etkileşimli olarak chatbot ile iletişim kurabilmesi için arayüz sağladı.  
- **Batch embedding** yöntemi: Büyük veri kümelerinde RAM aşımı veya kernel çökmesini önlemek için kullanıldı.

---

## 📈 Elde Edilen Sonuçlar

- Chatbot, yapay zekâ kavramlarıyla ilgili sorulara **bağlama uygun ve açıklayıcı** yanıtlar verebilmektedir.  
- Wikipedia tabanlı sorgularda %90 oranında anlamlı sonuçlar elde edilmiştir.  
- Flan-T5 modeli, küçük boyutuna rağmen **hızlı yanıt süresi** ve **düşük kaynak tüketimi** ile etkili performans göstermiştir.  
- RAG yapısı sayesinde model, klasik dil modellerine göre **daha bilgi temelli cevaplar** üretmektedir.

---

## 🛠️ Kurulum

1. Sanal ortamı aktif edin:
source ~/rag_env/bin/activate


2. Gerekli kütüphaneleri yükleyin.
pip install -r requirements.txt


3. Streamlit uygulamasını çalıştırın:
streamlit run app.py

4. Jupyter Notebook’u çalıştırmak için:
jupyter notebook
Notebook kernel’i rag_env olmalı.


📁 Dosya Yapısı
akbank/
│
├─ app.py               # Streamlit uygulaması
├─ AI-RAG-Notebook.ipynb         # Notebook
├─ data/
│   └─ Wikipedia_AI_Glossary.csv
└─ README.md


Web Uygulaması: https://ai-rag-chatbot-yusraazrademirel.streamlit.app
