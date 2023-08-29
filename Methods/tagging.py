import spacy


nlp_en = spacy.load("en_core_web_sm")
nlp_de = spacy.load("de_core_news_sm")
confidence_threshold = 0.2

tags = ["NNP", "NN"]
forbidden_dep = ["aux", "prep", "pcomp", "dobj", "pobj"]

def add_hashtags(text):
    doc_en = nlp_en(text)
    doc_de= nlp_de(text)
    
    Topics = set()
    for token in [doc_en,doc_de]:
        if token.dep_ in forbidden_dep:
            continue
        if token=="-":
            continue
        if token.tag_ in tags:
            Topics.append(f"#{token.lemma_}")
    
    return text+"\n"+"\n   ".join(Topics)

def create_table(sentence):
    hashtags = add_hashtags(sentence)
    doc = nlp_en(sentence)  # Default to English for token information

    if hashtags:
        detector = Detector(sentence, quiet=True)
        lang = detector.language.code

        if lang == "de":
            doc = nlp_de(sentence)
    
    table = f"{doc.lang.capitalize()}:\n"
    table += "|   TEXT   |   LEMMA   |  POS  |   DEP   |  HASH   |\n"
    table += "|:--------:|:---------:|:-----:|:-------:|:-------:|\n"
    
    for token in doc:
        if token.text in hashtags:
            table += f"|  {token.text}  |  {token.lemma_}  |  {token.pos_}  |  {token.dep_}  |  {hashtags[hashtags.index(token.text)]}  |\n"
    
    return table

if __name__ == "__main__":
    sentence = "I like trains because trains are cool."
    print(add_hashtags(sentence))
    table = create_table(sentence)
    print(table)
