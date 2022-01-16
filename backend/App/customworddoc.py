import docx
from docx.document import Document
from docx.text.paragraph import Paragraph
from docx.table import _Cell, Table
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P


def iter_block_items(parent):
    """
    Generate a reference to each paragraph and table child within *parent*,
    in document order. Each returned value is an instance of either Table or
    Paragraph. *parent* would most commonly be a reference to a main
    Document object, but also works for a _Cell object, which itself can
    contain paragraphs and tables.
    """
    if isinstance(parent, Document):
        parent_elm = parent.element.body
        # print(parent_elm.xml)
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    else:
        raise ValueError("something's not right")

    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)

#doc = docx.Document("nwhacks cover letter.docx")


# for block in iter_block_items(doc):
#     if isinstance(block, Table):
#         # is a table?
#         pass
#     else:
#         # is a paragraph?
#         print(block.text)


def find_curly(text, toBeReplaced, replace):
    line = text.split()
    print(line)
    for word in range(len(line)):

        noPuncWord = ""
        for char in line[word]:
            if ord(char) >= 65 and ord(char) <= 90:
                noPuncWord += char

            elif ord(char) >= 97 and ord(char) <= 122:
                noPuncWord += char

        if noPuncWord == toBeReplaced and (line[word][0] == "{" and (line[word][-1] == "}" or line[word][-2] == "}")):
            line[word] = replace

    line = " ".join(line)
    return line


print(find_curly(
    "May {{Name}} not turn out to be {{adjective}}.", "Name", "Kevin"))
