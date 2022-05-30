import constants
import checker
import re

def charsToTableTokens(code):
    openCode = open(code,"r")
    codeToString = openCode.read()
    #print("read the code")
    #print(codeToString)
    #print(re.split("[\s]+", codeToString))
    #_tokens = re.split(" ", codeToString)
    # =;\(\)\[\]\{\}
    #[=]|[\(]|[\)]
    _tokens = re.findall("[\d][\.][\d+]|\w+|[=;\(\)\[\]\{\}]+", codeToString)
    #_tokens = re.split("\w|",codeToString)
    #print("all chars in")
    #print(_tokens)
    tokens = []
    #print(len(_tokens[0]))
    for element in _tokens:
        if len(element)==0 or re.findall("[\d]+[\.][\d]+", element) ==[]:
            specialChar, char = checker.isSpeacialChar(element)
            if specialChar: 
                #print("elt ", element)
                tokens.append({"type": constants.specialChars[char]['symbol'],"value":element})
            else :
                tokens.append({"type":constants.typeWord, "value": element})
        else :
            tokens.append({"type": constants.typeNumber, "value": element})
    #print(re.findall("==", codeToString))
    #print("all tokens")
    #print(tokens)
    return tokens

code = "code.txt"
value = charsToTableTokens(code)

print(value)