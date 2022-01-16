# Import needed libraries
import requests
import json
from google.cloud import language

client = language.LanguageServiceClient.from_service_account_json('services.json')


def analyze_text_sentiment(text):
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = dict(
        text=text,
        score=f"{sentiment.score:.1%}",
        magnitude=f"{sentiment.magnitude:.1%}",
    )
    for k, v in results.items():
        print(f"{k:10}: {v}")

text = "Guido van Rossum is great!"
analyze_text_sentiment(text)