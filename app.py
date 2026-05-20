import gradio as gr
from utils.translate import translate_text
from utils.sentiment import get_sentiment
from utils.summarize import summarize_text
from utils.ner import extract_entities

LANGUAGE_MAP = {
    "Telugu": "te",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Japanese": "ja",
    "Arabic": "ar",
    "Chinese Simplified": "zh-CN",
    "Portuguese": "pt",
    "Russian": "ru",
}

SENTIMENT_EMOJI = {
    "positive": "😊",
    "negative": "😔",
    "neutral": "😐",
}


def run_pipeline(text, target_language):
    if not text or not text.strip():
        return "", "", "", "", "Please enter some text to analyze."

    target_code = LANGUAGE_MAP.get(target_language, "en")

    # Step 1: Translate to English
    try:
        english_text = translate_text(text, target_lang="en")
    except Exception as e:
        english_text = text
        english_error = f"[Translation to English failed: {e}]"
    else:
        english_error = None

    # Step 2: Translate to target language
    try:
        target_translation = translate_text(text, target_lang=target_code)
    except Exception as e:
        target_translation = f"[Translation to {target_language} failed: {e}]"

    # Step 3: Sentiment from English text
    try:
        label, score = get_sentiment(english_text)
        label_lower = label.lower()
        emoji = SENTIMENT_EMOJI.get(label_lower, "😐")
        confidence = round(score * 100, 1)
        sentiment_output = f"**{emoji} {label.capitalize()}** (confidence: {confidence}%)"
    except Exception as e:
        sentiment_output = f"[Sentiment analysis failed: {e}]"

    # Step 4: Summarize English text
    try:
        summary = summarize_text(english_text)
    except Exception as e:
        summary = f"[Summarization failed: {e}]"

    # Step 5: Named Entity Recognition
    try:
        entities = extract_entities(english_text)
        if entities:
            lines = [f"• **{ent['word']}** → {ent.get('entity_group', ent.get('entity', 'UNKNOWN'))}" for ent in entities]
            ner_output = "\n".join(lines)
        else:
            ner_output = "No named entities detected."
    except Exception as e:
        ner_output = f"[NER failed: {e}]"

    if english_error:
        english_text = f"{english_text}\n\n{english_error}"

    return english_text, target_translation, sentiment_output, summary, ner_output


EXAMPLES = [
    [
        "I absolutely loved the concert last night! The band was incredible and the crowd was amazing.",
        "Spanish",
    ],
    [
        "The service at this restaurant was terrible. The food was cold and the staff was rude.",
        "French",
    ],
    [
        "Apple Inc. announced a new iPhone model in Cupertino, California. CEO Tim Cook presented the device at the annual keynote event.",
        "German",
    ],
]

with gr.Blocks(theme=gr.themes.Soft(), title="Nexus AI — Multilingual NLP Platform") as demo:

    gr.Markdown(
        """
# 🤖 Nexus AI — Multilingual NLP Platform

**Multilingual text analysis powered by HuggingFace Transformers and deep-translator.**

Built by [Srikar Allampally](https://github.com/allampallysrikar) &nbsp;|&nbsp;
[GitHub Repository](https://github.com/allampallysrikar/nexus-ai)
        """
    )

    with gr.Row():
        with gr.Column(scale=2):
            input_text = gr.Textbox(
                label="Input Text",
                placeholder="Paste any text in any language...",
                lines=6,
            )
            target_language = gr.Dropdown(
                label="Target Language for Translation",
                choices=list(LANGUAGE_MAP.keys()),
                value="Spanish",
            )
            submit_btn = gr.Button("Analyze", variant="primary")

        with gr.Column(scale=3):
            english_output = gr.Textbox(label="English Translation", lines=4, interactive=False)
            target_output = gr.Textbox(label="Target Language Translation", lines=4, interactive=False)
            sentiment_output = gr.Markdown(label="Sentiment")
            summary_output = gr.Textbox(label="Summary", lines=3, interactive=False)
            ner_output = gr.Markdown(label="Named Entities")

    gr.Examples(
        examples=EXAMPLES,
        inputs=[input_text, target_language],
        label="Try these examples",
    )

    submit_btn.click(
        fn=run_pipeline,
        inputs=[input_text, target_language],
        outputs=[english_output, target_output, sentiment_output, summary_output, ner_output],
    )

    input_text.submit(
        fn=run_pipeline,
        inputs=[input_text, target_language],
        outputs=[english_output, target_output, sentiment_output, summary_output, ner_output],
    )

    gr.Markdown(
        """
---
*Nexus AI uses open-source NLP models. Results may vary by input language and text length.*
        """
    )

if __name__ == "__main__":
    demo.launch()
