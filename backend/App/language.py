# Import needed libraries
import requests
import json
from google.cloud import language_v1


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
            adjectives.append(text.content)

    return adjectives


print(get_adjectives("	1Password is looking for promising new programmers to join us and gain valuable experience in a well-established team of developers. Our team is a friendly and welcoming environment for programmers with all levels of experience. We will do our best to help you realize your potential as a developer. The hope is that you'll leave with a passion for learning, some new friends, and the self-confidence to take on whatever comes next."))
