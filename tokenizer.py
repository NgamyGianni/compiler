import constants
import checker
import re

def charsToTableTokens(code):
    openCode = open(code,"r")
    codeToString = checker.changeSymbolToString(openCode.read())
    print("Reading the code:\n")
    _tokens = re.findall("[\d][\.][\d+]|\w+|[=;\(\)\[\]\{\}]+", codeToString)
    tokens = []
    for element in _tokens:
        if len(element)== 0 or re.findall("^[\d]+$|^[\d+]\.[\d]+$", element) ==[]:
            specialChar = checker.isSpeacialChar(element)
            if specialChar:
                tokens.append({"type":element})
            else :
                tokens.append({"type":constants.typeWord, "value": element})
        else :
            tokens.append({"type": constants.typeNumber, "value": element})
    return tokens

# f = open("code.txt","r")
# code = f.read()
# print("before")
# print(code)
if __name__=="__main__":
    print("after")
    print(charsToTableTokens("code.js"))
#value = isSpeacialChar("==")
