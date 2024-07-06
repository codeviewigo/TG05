from translate import Translator


def translate_text(text, from_lang='en', to_lang='ru'):
    try:
        return Translator(from_lang=from_lang, to_lang=to_lang).translate(text)
    except:
        return 'Не удалось перевести текст'