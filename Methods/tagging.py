import spacy
import pandas as pd
import string

nlp_en = spacy.load("en_core_web_sm")
nlp_de = spacy.load("de_core_news_sm")

forbidden_token = set()
tags = ["NNP", "NN", "NNS", "NP", "NNPS"]
posis = ["NOUN", "PROPN"]

forbidden_dep = ["case", "nk", "c", "mo", "aux", "prep", "pcomp", "dobj", "pobj", "punct", "pnc", "nk"]
forbidden_tag = ["VAFIN", "APPR", "KON", "ADJD", "VVFIN", "KO", "ART", "NE", "ADJA", "XY", "ADJ", "AUX", "CONJ", "PRON", "ADP", "ADV", "DET", "INTJ", "NUM", "PART", "PRP"]
forbidden_pos = ["NUM"]

def keep_alphabet_characters(text):
    alphabet_characters = list(string.ascii_letters)  # Use string.ascii_letters for both upper and lower case
    alphabet_characters.extend([' ', '\t', 'ü', 'ä', 'ö'])
    filtered_text = ''.join([char for char in text if char in alphabet_characters])
    return filtered_text

def set_clean(my_set):
    cleaned_set = my_set.copy()

    for str1 in my_set:
        for str2 in my_set:
            if str1 < str2 and str2.startswith(str1):
                cleaned_set.discard(str1)
                continue
            if str1 > str2 and str1.startswith(str2):
                cleaned_set.discard(str2)
                continue
    return cleaned_set

def add_hashtags(text, onlytags=False, tag="#",flashcardmode=False):
    # Clean the text
    cleantext = keep_alphabet_characters(text)

    # Initialize current_topics
    current_topics = set()

    # Tokenize text in English and German
    doc_en = nlp_en(cleantext)
    doc_de = nlp_de(cleantext)

    # Process tokens
    for doc in [doc_de, doc_en]:
        for token in doc:
            if token.text.islower():
                continue

            if token.tag_ in forbidden_tag or token.dep_ in forbidden_dep or token.pos_ in forbidden_pos:
                forbidden_token.add(token.text)
                continue

            if token.tag_ in tags and token.pos_ in posis and len(token.text) > 2:
                current_topics.add(f"{tag}{token.lemma_}")

    # Remove forbidden tokens from current_topics
    current_topics -= forbidden_token

    # Clean current_topics
    current_topics = set_clean(current_topics)

    if onlytags:
        return "Tags & Topics:\n   " + "\n   ".join(list(current_topics))
    return text + "\n   Tags & Topics:\n   " + "\n   ".join(list(current_topics))

def gap_text(text):
    # Clean the text
    cleantext = keep_alphabet_characters(text)

    # Initialize current_topics
    current_topics = set()

    # Tokenize text in English and German
    doc_en = nlp_en(cleantext)
    doc_de = nlp_de(cleantext)

    # Process tokens
    for doc in [doc_de, doc_en]:
        for token in doc:

            if token.tag_ in forbidden_tag or token.dep_ in forbidden_dep or token.pos_ in forbidden_pos:
                forbidden_token.add(token.text)
                continue

            if token.tag_ in tags and token.pos_ in posis and len(token.text) > 2:
                print(token)
                current_topics.add(f"{token.text}")

    # Create gap text and flashcard
    gap_text = cleantext
    for token in current_topics:
        gap_text = gap_text.replace(token, "_" * len(token))

    flashcard = {
        "front": gap_text,
        "back": cleantext
    }

    return flashcard

if __name__ == "__main__":
    sentence = "### Produktionsseite- Wirtschaftlichkeit- einsatzsteuerung der Produktionsfaktoren -  Gegeben = Input Menge- Maximaler Output- gegeben= Output Menge- Ininmaler Input."
    print(add_hashtags(sentence))
