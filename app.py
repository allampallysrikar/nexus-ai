from flask import Flask, render_template, request, jsonify
from utils.translate import translate_text
from utils.sentiment import get_sentiment
from utils.summarize import summarize_text
from utils.ner import extract_entities

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "No text provided"}), 400
        
    text = data.get("text", "")
    target_lang = data.get("targetLanguage", "te") # Default to Telugu
    
    if not text.strip():
         return jsonify({"error": "Text is empty"}), 400

    result = {
        "original": text
    }

    try:
        # Step 1: Translate to English (as base for NLP models)
        english_translated = translate_text(text, target_lang='en')
        result['english_translation'] = english_translated
        
        # Target Translation
        target_translated = translate_text(text, target_lang=target_lang)
        result['target_translation'] = target_translated

        # Sentiment Analysis
        label, score = get_sentiment(english_translated)
        result['sentiment'] = {"label": label, "score": score}
            
        # Summarization
        summary = summarize_text(english_translated)
        result['summary'] = summary
            
        # Named Entity Recognition
        entities = extract_entities(english_translated)
        result['entities'] = entities

        return jsonify(result), 200
        
    except Exception as e:
        print("Error during analysis:", e)
        return jsonify({"error": "An error occurred during text analysis."}), 500

if __name__ == "__main__":
    app.run(debug=True)