import constants
import parserHelper
import parserConst
import parser
import tokenizer

def create(type, tokens, start):
        if type == "statementSwitch":
            return statementSwitch(tokens, start)
        elif type == "statementCase":
            return statementCase(tokens, start)

def definedMethod(tokens, start):
        if tokens[start+1]["type"] == constants.typeNumber:
            raise NameError(parserConst.exceptedErros[5])
        if tokens[start+2]["type"] != constants.specialChars["openParenthesis"]["value"]:
            raise NameError(parserConst.exceptedErros[6])

        arguments =[]
        numbParathensis = 1
        i = start+3
        while i<len(tokens):
            arguments.append(tokens[i])
            if tokens[i]["type"] == constants.specialChars["closeParenthesis"]["value"]:
                numbParathensis-=1
                break
        if numbParathensis !=0:
            raise NameError(parserConst.exceptedErros[0])
        return 0

   #check switch statement
def statementSwitch(tokens, start):
        end = 0
        argument = parserHelper.searchArgs(tokens, start+1)
        print(argument)
        if not tokens[argument["end"]+1]["type"] == constants.symbolOpenCurlyBrace:
            raise NameError(parserConst.parserConst["errorMissingOpeningBrace"])
        for i in range(start, len(tokens)):
            if tokens[i]["type"] == constants.symbolCloseCurlyBrace:
                end = i
                foundEnd = True
                break
        if not foundEnd:
            raise NameError(parserConst.parserConst["errorMissingBreakStatement"])
        return { "type" : parserConst.parserConst["statementSwitch"], "argument" : argument["args"], "start" : start, "end" : end, "varType" : argument["args"][0]["type"], "AST" : parser.parserFunc([], tokens, argument["end"]+2, end)}

    #check switch statement
def statementCase(tokens, start):
        switchType = "word"
        foundEnd = False
        end = 0
        if not tokens[start+1]["type"] == switchType:
            raise NameError(parserConst.parserConst["errorCaseInvalidType"])
        for i in range(start, len(tokens)):
            if tokens[i]["type"] == "word" and tokens[i]["value"] == "break":
                end = i
                foundEnd = True
                break
        if not foundEnd:
            raise NameError(parserConst.parserConst["errorMissingBreakStatement"])
        return { "type" : parserConst.parserConst["statementCase"], "value" : tokens[start+1]["value"], "start" : start, "end" : end , "AST" : parser.parserFunc([], tokens, start+2, end) }
    
def variableDeclaration(tokens, start):
        if tokens[start+1]["type"] != constants.typeWord:
            raise NameError(parserConst.parserConst["errorInvalidName"])
        
        variableName= tokens[start+1]["value"]
        return {"type": parserConst.expressionDeclaration, "variableName": variableName}

def variableAffectation(tokens, start):
        if tokens[start-1]["type"] != constants.typeWord :
            raise NameError(parserConst.parserConst["errorInvalidName"])
        
        variableName= tokens[start-1]["value"]
        variableValue= tokens[start+1]
        return {"type": parserConst.expressionAffectation, "variableName": variableName, "variableValue": variableValue}
    
tokens = [{'type': 'word', 'value': 'if'}, {'type': 'openParenthese'}, {'type': 'word', 'value': 'a'}, {'type': 'equalSame'}, {'type': 'number', 'value': '12'}, {'type': 'closeParenthese'}, {'type': 'word', 'value': ''}, {'type': 'openCurlyBrace'}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': 'var'}, {'type': 'word', 'value': 'p'}, {'type': 'equal'}, {'type': 'number', 'value': '3'}, {'type': 'semiColon'}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': 'if'}, {'type': 'openParenthese'}, {'type': 'word', 'value': 'b'}, {'type': 'equalSame'}, {'type': 'number', 'value': '3'}, {'type': 'closeParenthese'}, {'type': 'word', 'value': ''}, {'type': 'openCurlyBrace'}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': 'let'}, {'type': 'word', 'value': 'i'}, {'type': 'equal'}, {'type': 'number', 'value': '5'}, {'type': 'semiColon'}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'closeCurlyBrace'}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'closeCurlyBrace'}, {'type': 'word', 'value': ''}]

            