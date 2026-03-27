from transformers import pipeline

# Use a pre-trained BERT model for NER
ner_pipeline = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")

def extract_entities(text):
    try:
        if not text.strip():
            return []

        # Limit text length
        text = text[:1000]
        
        results = ner_pipeline(text)
        
        entities = []
        for r in results:
            entities.append({
                "entity": r['entity_group'],
                "word": r['word'],
                "score": round(float(r['score']), 2)
            })
            
        return entities
        
    except Exception as e:
        print("NER Error:", e)
        return []
