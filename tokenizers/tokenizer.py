

import constants
import checker
import re

def charsToTableTokens(code):
    openCode = open(code,"r")
    codeToString = checker.changeSymbolToString(openCode.read())
    print("Reading the code:\n")
    print(codeToString)
    #_tokens = re.findall("[\d][\.][\d+]|\w+|[=;\(\)\[\]\{\}]+", codeToString)
    _tokens = re.split("[\s]",codeToString)
    tokens = []
<<<<<<< HEAD
    # for element in _tokens:
    #     if len(element)==0 or re.findall("[\d]+[\.][\d]+", element) ==[]:
    #         specialChar = checker.isSpeacialChar(element)
    #         if specialChar:
    #             tokens.append({"type":element})
    #         else :
    #             tokens.append({"type":constants.typeWord, "value": element})
    #     else :
    #         tokens.append({"type": constants.typeNumber, "value": element})
    for elt in _tokens:
        if len(elt) == 0 or re.findall("[\d]+|[\d]+[\.][\d]+", elt) == []:
            specialChar = checker.isSpeacialChar(elt)
=======
    for element in _tokens:
        if len(element)==0 or re.findall("[\d]+|[\d+]\.[\d]+", element) ==[]:
            specialChar = checker.isSpeacialChar(element)
>>>>>>> a12ec093b6beda4f25cb3381143bdd879527c317
            if specialChar:
                tokens.append({"type":elt})
            else :
                tokens.append({"type":constants.typeWord, "value": elt})
        else :
            tokens.append({"type": constants.typeNumber, "value": elt})
    return tokens

# f = open("code.txt","r")
# code = f.read()
# print("before")
# print(code)
if __name__=="__main__":
    print("after")
    print(charsToTableTokens("code.txt"))
#value = isSpeacialChar("==")
