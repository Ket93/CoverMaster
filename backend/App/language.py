# Import needed libraries
import requests
import json
from google.cloud import language_v1


def analyze_text_sentiment(text):
    client = language_v1.LanguageServiceClient.from_service_account_json(
        'backend/App/services.json')
    document = language_v1.Document(
        content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = round(round(sentiment.score, 2) *
                    round(sentiment.magnitude, 2), 2)
    return results


def get_adjectives(text_content):
    adjectives = []
    client = language_v1.LanguageServiceClient.from_service_account_json(
        'backend/App/services.json')
    #client = language_v1.LanguageServiceClient.from_service_account_json('services.json')

    # text_content = 'This is a short sentence.'

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_syntax(
        request={'document': document, 'encoding_type': encoding_type})

    for token in response.tokens:
        text = token.text
        part_of_speech = token.part_of_speech
        wordtype = language_v1.PartOfSpeech.Tag(part_of_speech.tag).name
        if wordtype == "ADJ":
            adjectives.append(
                [text.content, analyze_text_sentiment(text.content)])

    adjectives = list(reversed(sorted(adjectives, key=lambda x: x[1])))
    print(adjectives)
    return adjectives
