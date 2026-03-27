import os
import requests

API_URL = "https://api-inference.huggingface.co/models/dslim/bert-base-NER"
HF_TOKEN = os.environ.get("HF_TOKEN")

def extract_entities(text):
    try:
        if not text.strip():
            return []

        headers = {"Authorization": f"Bearer {HF_TOKEN}"} if HF_TOKEN else {}
        payload = {"inputs": text[:1000]}
        
        response = requests.post(API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            results = response.json()
            entities = []
            for r in results:
                entity_group = r.get('entity_group') or r.get('entity', 'UNKNOWN')
                entities.append({
                    "entity": entity_group,
                    "word": r.get('word', ''),
                    "score": round(float(r.get('score', 0.0)), 2)
                })
            
            # Simple aggregation to combine subwords
            merged = []
            for ent in entities:
                if merged and ent['word'].startswith('##') and merged[-1]['entity'].replace('B-','').replace('I-','') == ent['entity'].replace('B-','').replace('I-',''):
                    merged[-1]['word'] += ent['word'][2:]
                else:
                    merged.append(ent)
                    
            return merged
        else:
            print("HF API Error:", response.text)
            return []
            
    except Exception as e:
        print("NER Error:", e)
        return []
