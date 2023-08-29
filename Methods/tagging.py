import spacy
import pandas as pd

nlp_en = spacy.load("en_core_web_sm")
nlp_de = spacy.load("de_core_news_sm")
confidence_threshold = 0.2

tags = ["NNP", "NN","NNS"]
forbidden_dep = ["aux", "prep", "pcomp", "dobj", "pobj"]

def add_hashtags(text):
    doc_en = nlp_en(text)
    doc_de= nlp_de(text)
    
    topics = set()
    for doc in [doc_en, doc_de]:
        for token in doc:
            if token.dep_ in forbidden_dep:
                continue
            if token.text == "-":
                continue
            if token.tag_ in tags:
                topics.add(f"#{token.lemma_}")

    return text + "\n" + "\n   ".join(topics)

def create_table(sentence):
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
    sentence = "I like trains because trains are cool."
    print(add_hashtags(sentence))
    table = create_table(sentence)
    print(table)
