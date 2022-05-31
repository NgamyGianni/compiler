#from asyncio import constants
import parserConst
import constants
def searchArgs(tokens, start):
    print(tokens[start]["type"],constants.symbolOpenParenthesis)
    if not tokens[start]["type"] == constants.symbolOpenParenthesis:
        raise NameError(parserConst.parserConst["errorMissingOpenParenthesis"])
    foundEnd = False
    end = 0
    args = []
    for i in range(start, len(tokens)):
        if tokens[i]["type"] == constants.symbolCloseParenthesis:
            foundEnd = True
            end = i
            break
        elif tokens[i]["type"] == "word":
            args.append({ "type" : "word", "name" : tokens[i]["value"] })
        elif tokens[i]["type"] == "number":
            args.append({ "type" : "number", "name" : tokens[i]["value"] })

    if not foundEnd:
        raise NameError(parserConst.parserConst["errorMissingClosingParenthesis"])
    if len(args) == 0:
        raise NameError(parserConst.parserConst["errorEmptyArguments"])

    return { "args" : args, "end" : end }

def searchCloseCurlBrace(tokens, start):
    countCurlBrace = 1
    if start == len(tokens):
        raise NameError(parserConst.parserConst["errorExeceptCurlBrace"])
    i = start+1
    while i<len(tokens):
        if tokens[i]["type"]==constants.symbolCloseCurlyBrace :
            print("reduce count")
            countCurlBrace-=1
        
        if tokens[i]["type"] == constants.symbolOpenCurlyBrace:
            print("add count")
            countCurlBrace+= 1
        
        if countCurlBrace == 0:
            break
        i += 1
    if countCurlBrace!=0:
        raise NameError(parserConst.parserConst["errorMissingClosingBrace"])
    end = i
    return {"start":start, "end":end}


