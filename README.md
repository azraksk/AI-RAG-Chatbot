# AI-RAG Chatbot

## Projenin Amacı
Bu proje, Wikipedia AI Glossary veri setini kullanarak bir **Retrieval-Augmented Generation (RAG) Chatbot** oluşturmayı amaçlamaktadır. Kullanıcı sorularını doğal dilde yanıtlamak ve teknik terimler hakkında bilgi vermek hedeflenmiştir.

## Veri Seti
Kullanılan veri seti: [Wikipedia AI Glossary](https://www.kaggle.com/datasets/antoinebourgois2/wikipedia-ai-glossary)  
- Veri seti, yapay zekâ ile ilgili terimlerin açıklamalarını içerir.  
- Projede veri seti **GitHub reposuna eklenmemiştir**, uygulama çalıştırılırken Kaggle API üzerinden indirilmektedir.

## Kullanılan Yöntemler
- **Embedding Oluşturma:** Wikipedia AI Glossary’den alınan metinler vektör uzayına dönüştürülür.  
- **Retrieval (Sorgulama) Mekanizması:** Kullanıcının sorusu embedding’e dönüştürülür ve veri setindeki en benzer terimler bulunur.  
- **OpenAI API ile Yanıt Üretme:** Seçilen terim açıklamaları kullanılarak doğal dil yanıtı üretilir.  
- **Streamlit Kullanımı:** Chatbot arayüzü Streamlit ile hazırlanmıştır.  

## Elde Edilen Sonuçlar
- Kullanıcı sorularına doğru ve anlamlı yanıtlar üretebilen bir chatbot oluşturulmuştur.  
- Teknik terimler ve AI ile ilgili kavramlar hakkında bilgi sunabilmektedir.  
- Uygulama hem yerel ortamda hem de internette Streamlit üzerinden çalıştırılabilir.

## Canlı Web Uygulaması
[AI-RAG Chatbot Web](https://ai-rag-chatbot-yusraazrademirel.streamlit.app)

---

## 🛠️ Kurulum

1. Reposu klonlayın:
```bash
git clone https://github.com/azraksk/AI-RAG-Chatbot.git
cd AI-RAG-Chatbot
```

2. Gerekli kütüphaneleri yükleyin.
```bash
pip install -r requirements.txt
```

3. Kaggle API anahtarınızı bilgisayarınıza ekleyin:
Kaggle’dan kaggle.json dosyasını indirin.
Terminalde şu komutları çalıştırın:

```bash
mkdir -p ~/.kaggle
mv ~/Desktop/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

4. Streamlit uygulamasını çalıştırın:

```bash
streamlit run app.py
```

5. Jupyter Notebook’u çalıştırmak için:

```bash
jupyter notebook
```
Notebook kernel’i rag_env olmalıdır.



📁 Dosya Yapısı:

AI-RAG-Chatbot/
│
├── data/
│   ├── Wikipedia_AI_Glossary.csv
│   └── wikipedia-ai-glossary.zip
│
├── .gitignore
├── AI-RAG-Notebook.ipynb
├── README.md
├── app.ipynb
├── app.py
└── requirements.txt


Web Uygulaması: https://ai-rag-chatbot-yusraazrademirel.streamlit.app
