import spacy

web_core = "_core_web_sm"
news_core = "_core_news_sm"

LANGUAGES = ["en", "de", "es", "fr", "it", "nl", "pt","da", "el", "lt", "no", "pl", "ro"]
#LANGUAGES = ["en"]
LANGUAGE_DICTS = {}

for lang in LANGUAGES:
    try:
        if lang == "no":
            LANGUAGE_DICTS["no"] = spacy.load("nb" + web_core)
        else:
            LANGUAGE_DICTS[lang] = spacy.load(lang + web_core)
    except:
        if lang == "no":
            LANGUAGE_DICTS["no"] = spacy.load("nb" + news_core)
        else:
            LANGUAGE_DICTS[lang] = spacy.load(lang + news_core)