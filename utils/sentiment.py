from transformers import pipeline

# Use better GENERAL model (not just reviews)
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment"
)

def get_sentiment(text):
    try:
        if not text.strip():
            return "NEUTRAL", 0.0

        # Limit text length (VERY IMPORTANT)
        text = text[:512]

        result = sentiment_pipeline(text)[0]

        label_map = {
            "LABEL_0": "NEGATIVE",
            "LABEL_1": "NEUTRAL",
            "LABEL_2": "POSITIVE"
        }

        label = label_map[result['label']]
        score = round(result['score'], 2)

        return label, score

    except Exception as e:
        print("Sentiment Error:", e)
        return "UNKNOWN", 0.0