#from asyncio import constants
import parserConst
from ..tokenizer import constants
def searchArgs(tokens, start):
    if not tokens[start]["type"] == "(":
        raise NameError(parserConst["errorMissingOpenParenthesis"])
    foundEnd = False
    end = 0
    args = []
    for i in range(start, len(tokens)):
        if tokens[i]["type"] == ")":
            foundEnd = True
            end = i
            break
        elif tokens[i]["type"] == "word":
            args.append({ "type" : "word", "name" : tokens[i]["value"] })
        elif tokens[i]["type"] == "number":
            args.append({ "type" : "number", "name" : tokens[i]["value"] })

    if not foundEnd:
        raise NameError(parserConst["errorMissingClosingParenthesis"])
    if len(args) == 0:
        raise NameError(parserConst["errorEmptyArguments"])

    return { "args" : args, "end" : end }

def searchCloseCurlBrace(tokens, start):
    countCurlBrace = 1
    if start == len(tokens):
        raise NameError(parserConst["errorExeceptCurlBrace"])
    i = start
    while i<len(tokens):
        i+=1
        if tokens[i]["type"]==constants.symbolCloseCurlyBrace :#constants.symbolCloseCurlyBrace:
            countCurlBrace-=1
            break
    if countCurlBrace!=0:
        raise NameError(parserConst["errorExeceptCurlBrace"])
    end = i
    return {"start":start, "end":end}


