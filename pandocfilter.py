from panflute import *
from sys import *

headers = []


def bold(doc):
    doc.replace_keyword("BOLD", Strong(Str("BOLD")))
    doc.replace_keyword("bold", Strong(Str("bold")))

def duplicate_headers(elem, doc):
    if type(elem) == Header:
        text = stringify(elem)
        print("Duplicate headers!!!", file=stderr) if text in headers else headers.append(text)

def upper_str(elem, doc):
    if type(elem) == Str:
        elem.text = elem.text.upper()


def upper_header(elem, doc):
    if type(elem) == Header and elem.level > 2:
        return elem.walk(upper_str)


if __name__ == "__main__":
    run_filters([upper_header, duplicate_headers], prepare=bold)