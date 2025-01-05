import nlpcloud

def ner(text,search):
    client = nlpcloud.Client("finetuned-llama-3-70b", "a738af5249379e544877de7afdc34ab0ec1a198a", gpu=True)
    response = client.entities(
        text,
        searched_entity=search
    )
    return response

def sentiment_analysis(text):
    client = nlpcloud.Client("finetuned-llama-3-70b", "a738af5249379e544877de7afdc34ab0ec1a198a", gpu=True)
    response = client.sentiment(
        text,
        target="NLP Cloud"
    )
    return response

def language_detection(text):
    client = nlpcloud.Client("python-langdetect", "a738af5249379e544877de7afdc34ab0ec1a198a", gpu=False)
    client.lang_detection(
        text
    )