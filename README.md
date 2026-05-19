---
title: Nexus AI
emoji: 🤖
colorFrom: purple
colorTo: blue
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
---

# 🤖 Nexus AI — Multilingual NLP Platform

A world-class, responsive NLP web application built with **Flask**, **Vanilla JavaScript**, and **HuggingFace Transformers**. Perform Translation, Sentiment Analysis, Text Summarization, and Named Entity Recognition — all in one seamless glassmorphic interface.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=black)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

---

## ✨ Features

| Feature | Model Used | Description |
|---------|-----------|-------------|
| 🌍 **Translation** | `deep-translator` | Translate text from any language to English or a target language |
| 😊 **Sentiment Analysis** | `cardiffnlp/twitter-roberta-base-sentiment` | Classifies text as Positive, Negative, or Neutral with confidence score |
| 📝 **Summarization** | `sshleifer/distilbart-cnn-12-6` | Condenses long text into concise summaries |
| 🏷️ **Named Entity Recognition** | `dslim/bert-base-NER` | Extracts people, organizations, and locations from text |

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- pip
- ~2GB free disk space (for HuggingFace model downloads)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/allampallysrikar/nexus-ai.git
   cd nexus-ai
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   ```
   http://localhost:5000
   ```

> ⚠️ **First run note:** HuggingFace models will download automatically (~400MB total). This takes a few minutes on first launch. Subsequent runs are instant.

---

## 🏗️ Project Structure

```
nexus-ai/
├── app.py               # Flask application entry point
├── requirements.txt     # All dependencies
├── vercel.json          # Deployment configuration
├── static/
│   ├── css/             # Glassmorphic dark-mode styles
│   └── js/              # Async frontend logic
├── templates/           # HTML templates
└── utils/
    ├── ner.py           # Named Entity Recognition
    ├── sentiment.py     # Sentiment Analysis
    ├── summarize.py     # Text Summarization
    └── translate.py     # Translation
```

---

## 🛠️ Built With

- **Backend:** Python 3, Flask
- **Frontend:** HTML5, Vanilla CSS3 (Glassmorphism), Vanilla JavaScript
- **AI Models (HuggingFace Transformers):**
  - `cardiffnlp/twitter-roberta-base-sentiment` — Sentiment
  - `sshleifer/distilbart-cnn-12-6` — Summarization
  - `dslim/bert-base-NER` — Named Entity Recognition
- **Translation:** `deep-translator`

---

## 📬 Contact

Built by [Srikar Allampally](https://github.com/allampallysrikar) · allampallysrikar2005@gmail.com
