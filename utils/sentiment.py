import os
import requests

API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"
HF_TOKEN = os.environ.get("HF_TOKEN")

def get_sentiment(text):
    try:
        if not text.strip():
            return "NEUTRAL", 0.0

        headers = {"Authorization": f"Bearer {HF_TOKEN}"} if HF_TOKEN else {}
        payload = {"inputs": text[:512]}
        
        response = requests.post(API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            result = response.json()[0][0] # HuggingFace returns lists of lists
            
            # Map labels
            label_map = {"LABEL_0": "NEGATIVE", "LABEL_1": "NEUTRAL", "LABEL_2": "POSITIVE"}
            label = label_map.get(result.get('label', 'LABEL_1'), "NEUTRAL")
            score = round(result.get('score', 0.0), 2)
            
            return label, score
        else:
            print("HF API Error:", response.text)
            return "UNKNOWN", 0.0

    except Exception as e:
        print("Sentiment Error:", e)
        return "ERROR", 0.0