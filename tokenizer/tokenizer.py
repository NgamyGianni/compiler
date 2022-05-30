import constants
import checker
import re

def charsToTableTokens(code):
    openCode = open(code,"r")
    codeToString = openCode.read()
    print("Reading the code:\n")
    print(codeToString)
    _tokens = re.findall("[\d][\.][\d+]|\w+|[=;\(\)\[\]\{\}]+", codeToString)
    tokens = []
    for element in _tokens:
        if len(element)==0 or re.findall("[\d]+[\.][\d]+", element) ==[]:
            specialChar = checker.isSpeacialChar(element)
            if specialChar:
                tokens.append({"type":element})
            else :
                tokens.append({"type":constants.typeWord, "value": element})
        else :
            tokens.append({"type": constants.typeNumber, "value": element})
    return tokens
