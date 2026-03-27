from deep_translator import GoogleTranslator

def translate_text(text, target_lang='en'):
    try:
        if not text.strip():
            return ""

        # Auto detect → target_lang
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        return translated

    except Exception as e:
        print("Translation Error:", e)
        return text