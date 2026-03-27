import os
import requests

API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
HF_TOKEN = os.environ.get("HF_TOKEN")

def summarize_text(text):
    try:
        if not text.strip():
            return "Text is empty."
            
        words = text.split()
        if len(words) < 30:
            return "Text is too short to summarize (minimum 30 words required)."

        headers = {"Authorization": f"Bearer {HF_TOKEN}"} if HF_TOKEN else {}
        
        input_len = len(words)
        max_len = min(130, int(input_len * 0.6))
        min_len = min(30, int(input_len * 0.2))
        
        payload = {
            "inputs": text[:3000],
            "parameters": {"max_length": max_len, "min_length": min_len, "do_sample": False}
        }
        
        response = requests.post(API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            return response.json()[0].get('summary_text', "Summary generation failed.")
        else:
            print("HF API Error:", response.text)
            # Check if model is loading
            if "is currently loading" in response.text:
                return "The HuggingFace model is currently loading... Please try again in 20 seconds."
            return "API Error or Rate Limited. Please try again later."
            
    except Exception as e:
        print("Summarization Error:", e)
        return "Summarization failed."
