import spacy
import pandas as pd

nlp_en = spacy.load("en_core_web_sm")
nlp_de = spacy.load("de_core_news_sm")
confidence_threshold = 0.2

forbidden_token = set()
tags = ["NNP", "NN", "NNS","NP","NNPS"]
posis=["NOUN","PROPN"]

forbidden_dep = ["case","nk","c","mo","aux", "prep", "pcomp", "dobj", "pobj", "punct", "pnc", "nk"]
forbidden_tag = ["VAFIN","APPR","KON","ADJD","VVFIN","KO", "ART", "NE", "ADJA", "XY", "ADJ", "AUX", "CONJ", "PRON", "ADP", "ADV", "DET", "INTJ", "NUM", "PART","PRP"]
forbidden_pos =["NUM"]

def add_hashtags(text):
    current_topics = set()

    doc_en = nlp_en(text)
    doc_de = nlp_de(text)

    for doc in [doc_de, doc_en]:
        for token in doc:
            if token.text in forbidden_token or token.text.islower():
                continue

            if token.tag_ in forbidden_tag or token.dep_ in forbidden_dep or token.pos_ in forbidden_pos:
                #print(f"detected {token.text} as {token.tag_} {token.dep_} {token.pos_}")
                forbidden_token.add(token.text)
                continue

            if token.tag_ in tags and token.pos_ in posis and len(token.text)<3:
                current_topics.add(f"#{token.lemma_}")
    current_topics -= forbidden_token  # Remove forbidden tokens from current_topics
    return text + "\n   Tags & Topics:"+"\n   " + "\n   ".join(current_topics)

def create_table(sentence):
    # Note: The following two lines of code overwrite the same variable 'doc'
    doc = nlp_en(sentence)  # Default to English for token information
    doc = nlp_de(sentence)

    data = {
        "TEXT": [],
        "LEMMA": [],
        "POS": [],
        "TAG": [],
        "DEP": [],
    }

    for token in doc:
        data["TEXT"].append(token.text)
        data["LEMMA"].append(token.lemma_)
        data["POS"].append(token.pos_)
        data["TAG"].append(token.tag_)
        data["DEP"].append(token.dep_)

    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    sentence = "### Produktionsseite- Wirtschaftlichkeit- einsatzsteuerung der Produktionsfaktoren -  Gegeben = Input Menge- Maximaler Output- gegeben= Output Menge- Ininmaler Input."
    print(add_hashtags(sentence))
    table = create_table(sentence)
    print(table)
