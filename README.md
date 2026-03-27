# Nexus AI - Multilingual NLP Platform

A world-class, responsive NLP web application built with Flask, vanilla JavaScript, and HuggingFace Transformers. This platform uses state-of-the-art AI models to provide Translation, Sentiment Analysis, Text Summarization, and Named Entity Recognition all in one seamless interface.

## 🌟 Features
- **Multilingual Support**: Translates text from any language into English and various target languages.
- **Sentiment Analysis**: Evaluates the emotional tone of text (Positive, Negative, Neutral) using RoBERTa.
- **Text Summarization**: Condenses long articles or text into concise summaries using DistilBART.
- **Named Entity Recognition (NER)**: Extracts people, organizations, locations, and abstract concepts using BERT.
- **Premium UI**: Glassmorphic dark mode design, asynchronous fetching, and micro-animations.

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Access the platform:**
   Open your browser and navigate to `http://localhost:5000`

## 🛠️ Built With
- **Backend**: Python, Flask
- **Frontend**: HTML5, Vanilla CSS3 (Glassmorphism), Vanilla JavaScript
- **AI Models**: HuggingFace Transformers (`cardiffnlp/twitter-roberta-base-sentiment`, `sshleifer/distilbart-cnn-12-6`, `dslim/bert-base-NER`)
- **Translation**: `deep-translator`
