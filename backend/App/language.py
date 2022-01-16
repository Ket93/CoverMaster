# Import needed libraries
import requests
import json
from google.cloud import language_v1


# Import needed libraries
from posixpath import split
import requests
import json
from google.cloud import language_v1

def analyze_text_sentiment(text):
    client = language_v1.LanguageServiceClient.from_service_account_json(
        'backend/App/services.json')
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = [round(round(sentiment.score, 2) * round(sentiment.magnitude, 2), 2)]
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
            adjectives.append([text.content, analyze_text_sentiment(text.content)])


    adjectives = list(reversed(sorted(adjectives, key=lambda x:x[1])))
    return adjectives
    


print(get_adjectives("AdHawk Microsystems is changing the way that humans interact with computers by introducing microsystems that can detect eye movements with unprecedented resolution, speed, and power efficiency. Our eye tracking sensors will transform the way people use Virtual and Augmented Reality (VR/AR) technology through foveated rendering, intuitive and seamless UI design, and enhanced immersion. We are a fully funded startup with an experienced management team that believes in the ability of co-op candidates to make a significant contribution - in fact, AdHawk's founding team members have all been UW engineering coop students in the past. We believe in a flexible work environment with an emphasis on results and outcomes--not hours.  Our team consists of researchers, Ph. D.'s, and engineers of the highest caliber with a deep sense of curiosity and a passion for the technology we develop. We publish award-winning research papers, fabricate custom silicon chips at leading foundries and push the boundaries of physics and manufacturing to develop products that create compelling value for our customers.The successful candidate would gain hands-on experience working on current and future MEMS products. Work topics include but not limited to: mechanical design and 3D printing, test design and implementation, optical system testing, automated data collection and statistical analysis.. New ideas and exploratory work are encouraged. Learning is part of AdHawk's culture and our cross-disciplinary team is always happy to share knowledge with interested students. Perks of working at AdHawk include: free lunches, drinks, and snacks every day, table tennis, rock climbing, and VR gaming. We are located near campus and not far from an LRT stop. We look forward to working with creative, enthusiastic students in an exciting startup environment!"))
