from ast import arguments
import constants
import parserHelper
import parserConst
import parser
#import tokenizer


def create(type, tokens, start):
    if type == parserConst.statementSwitch:
        return statementSwitch(tokens, start)
    elif type == parserConst.statementCase:
        return statementCase(tokens, start)
    elif type == parserConst.declarationFunction:
        return definedMethod(tokens, start)
    elif type in parserConst.declarationVariable:
        return variableDeclaration(tokens, start)
    elif type == constants.symbolEqual:
        return variableAffectation(tokens, start)

def definedMethod(tokens, start):
        if tokens[start+1]["type"]!=constants.typeWord:
            raise NameError(parserConst["errorExceptedfunctionName"])
        arguments = parserHelper.searchArgs(tokens,start+2)
        brace = parserHelper.searchCloseCurlBrace(tokens, arguments["end"]+1)
        
        return {"type": parserConst.declarationFunction, "argument": arguments["args"], "start": start, "end": brace["end"], "varType": arguments["args"][0]["type"], "AST": parser.parserFunc([], tokens, arguments["end"]+2, brace["end"])}
        
# check switch
def statementSwitch(tokens, start):
        end = 0
        argument = parserHelper.searchArgs(tokens, start+1)
        print(argument)
        if not tokens[argument["end"]+1]["type"] == constants.symbolOpenCurlyBrace:
            raise NameError(parserConst.parserConst["errorMissingOpeningBrace"])
        
        brace = parserHelper.searchCloseCurlBrace(tokens,argument["end"]+1)
        return {"type": parserConst.statementSwitch, "argument": argument["args"], "start": start, "end": brace["end"], "varType": argument["args"][0]["type"], "AST": parser.parserFunc([], tokens, argument["end"]+2, brace["end"])}

#check switch statement
def statementCase(tokens, start):
        switchType = "word"
        foundEnd = False
        end = 0
        if not tokens[start+1]["type"] == switchType:
            raise NameError(parserConst.parserConst["errorCaseInvalidType"])
        for i in range(start, len(tokens)):
            if tokens[i]["type"] == "word" and tokens[i]["value"] == "break":
                end = i+1
                foundEnd = True
                break
        if not foundEnd:
            raise NameError(parserConst.parserConst["errorMissingBreakStatement"])
        return { "type" : parserConst.statementCase, "value" : tokens[start+1]["value"], "start" : start, "end" : end , "AST" : parser.parserFunc([], tokens, start+2, end) }

   
def variableDeclaration(tokens, start):
        if tokens[start+1]["type"] != constants.typeWord:
            raise NameError(parserConst.parserConst["errorInvalidName"])
        
        variableName= tokens[start+1]["value"]
        return {"type": parserConst.expressionDeclaration, "variableName": variableName, "end" : start+1}

def variableAffectation(tokens, start):
        if tokens[start-1]["type"] != constants.typeWord :
            raise NameError(parserConst.parserConst["errorInvalidName"])
        
        variableName= tokens[start-1]["value"]
        variableValue= tokens[start+1]
        return {"type": parserConst.expressionAffectation, "variableName": variableName, "variableValue": variableValue, "end" : start+1}
    
