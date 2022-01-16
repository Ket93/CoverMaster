from __future__ import print_function
from mailmerge import MailMerge
from datetime import date
from monkeylearn import MonkeyLearn
import os


# data = [
#     "Setup backup of computers. Maintain website. Setup and maintain other equipment. Set up forms using Microsoft Excel. Set up auto billing in QuickBooks. Manage and maintain software (i.e. Microsoft 365 & Adobe). Streamline manual tasks into digital time efficiencies (i.e. billing)"]

# ml = MonkeyLearn('4a5dea1a145f57159b3373fc5896acc1f507d5a7')
# model_id = 'ex_YCya9nrn'
# result = ml.extractors.extract(model_id, data)
# keywords = []

# for i in result.body[0]["extractions"]:
#     keywords.append(i["parsed_value"])


# Writing to the word doc

def writeDoc(data, id, adjectives):
    # template = os.path.abspath(
    #    'App/Mock Cover Letter.docx').replace("\\", "/")
    template = 'backend/App/Mock Cover Letter.docx'
    document = MailMerge(template)
    # print(document.get_merge_fields()) show all merged fields in Word doc

    document.merge(
        Date='{:%d-%b-%Y}'.format(date.today()),
        companyName=data["companyName"],
        Address=data["jobAddress"],
        City=data["jobCity"],
        Province=data["jobProvince"],
        Country=data["jobCountry"],
        postalCode=data["jobPostal"],
        adj1=adjectives[0][0],
        char1=adjectives[1][0],
        adj2=adjectives[2][0],
        trait1=adjectives[3][0],
        trait2=adjectives[4][0]
    )

    print(adjectives[0][0])
    print(adjectives[1][0])
    print(adjectives[2][0])
   # print(adjectives[3][0])
   # print(adjectives[4][0])
    document.write("test-output.docx")
    document.write(f"{id}.docx")
