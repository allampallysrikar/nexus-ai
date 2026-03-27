from transformers import pipeline

# Use a small summarization model for fast execution
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text):
    try:
        if not text.strip():
            return "Text is empty."
            
        words = text.split()
        if len(words) < 30:
            return "Text is too short to summarize (minimum 30 words required)."

        # Limit text to model max length if needed (around 1024 tokens)
        text = text[:3000] # Approximate char length for tokens
        
        # Adjust max_length based on input length
        input_len = len(text.split())
        max_len = min(130, int(input_len * 0.6))
        min_len = min(30, int(input_len * 0.2))
        
        # Avoid min_len >= max_len
        if min_len >= max_len:
            min_len = max_len - 5
            if min_len < 5:
                min_len = 5
        
        summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
        return summary[0]['summary_text']
        
    except Exception as e:
        print("Summarization Error:", e)
        return "Summarization failed."
