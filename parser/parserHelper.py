#from asyncio import constants
import parserConst
import os
import sys
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])
#print(os.path.split(libdir))
from tokenizers import constants
#from tokenizers import tokenizer


def searchArgs(tokens, start):
    if tokens[start]["type"] != "openParenthese":
        raise NameError(parserConst["errorMissingOpenParenthesis"])
    findEnd = False
    end = 0
    args = []
    for i in range(len(tokens)):
        if tokens[i]["type"] == "symboleCloseParenthesis":
            findEnd = True
            end = i
            break;
        elif tokens[i]["type"] == "typeWord":
            args.append({ "type" : "variable", "name" : tokens[i]["name"] })
        elif tokens[i]["type"] == "typeNumber":
            args.append({ "type" : "variable", "name" : tokens[i]["name"] })

    if not findEnd:
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
        elif tokens[i]["type"] == constants.symbolOpenCurlyBrace:
            countCurlBrace+=1
        if countCurlBrace == 0:
            break
    if countCurlBrace!=0:
        raise NameError(parserConst["errorExeceptCurlBrace"])
    end = i
    return {"start":start, "end":end}



