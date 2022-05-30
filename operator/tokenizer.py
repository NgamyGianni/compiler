import constants
import checker
import re

def charsToTableTokens(code):
    openCode = open(code,"r")
    codeToString = openCode.read()
    print("read the code")
    print(codeToString)
    #print(re.split("[\s]+", codeToString))
    _tokens = re.split("[\s]", codeToString)
    print("all chars in")
    print(_tokens)
    tokens = []
    print(_tokens)
    for element in range(len(tokens)):
        if len(element)==0 or re.findall("([\d]+[\.][\d]+", element):
            specialChar = checker.isSpeacialChar(element)
            if specialChar: 
                tokens.append({"type":element})
            else :
                tokens.append({"type":constants.typeWord, "value": element})
        else :
            tokens.append({"type": constants.typeNumber, "value": element})
    #print(re.findall("==", codeToString))
    print(tokens)
    return 0

code = "code.txt"
value = charsToTableTokens(code)
#print(float("100a"))
