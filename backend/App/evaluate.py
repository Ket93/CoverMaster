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

    if data["name"] == "undefined":
        data["name"] = "[Full Name]"

    if data["email"] == "undefined":
        data["email"] = "[Email]"

    if data["phone"] == "undefined":
        data["phone"] = "[Phone]"

    if data["address"] == "undefined":
        data["address"] = "[Address]"

    if data["zip"] == "undefined":
        data["zip"] = "[Postal Code]"

    if os.path.isfile(os.path.abspath(
           'customtemplate.docx')):
        template = os.path.abspath(
            'customtemplate.docx').replace("\\", "/")
    #    call custom merge functions here with template
    else:
        template = os.path.abspath(
           'App/Mock Cover Letter.docx').replace("\\", "/")
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
            adj1=adjectives[0][0].lower(),
            char1=adjectives[1][0].lower(),
            adj2=adjectives[2][0].lower(),
            trait1=adjectives[3][0].lower(),
            trait2=adjectives[4][0].lower(),
            Phone=data["phone"],
            Email=data["email"],
            Name=data["name"],
            personalAddress=data["address"],
            personalPostal=data["zip"]
        )
    # template = 'backend/App/Mock Cover Letter.docx'


    document.write("test-output.docx")
    document.write(f"{id}.docx")
