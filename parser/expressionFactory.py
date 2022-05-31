import parserConst
<<<<<<< HEAD
import os
import sys
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])
#print(os.path.split(libdir))
#from tokenizers import constants
import parserHelper
from tokenizers import tokenizer
# from ast import operator




def statementSwitch(tokens, start):
    print(tokens[start])

def definedMethod(tokens, start):
    args = parserHelper.searchArgs(tokens, start)

    # if tokens[start+1]["type"] == constants.typeNumber:
    #     raise NameError(parserConst["errorExeceptParenthesis"])
    # if tokens[start+2]["type"] != constants.specialChars["openParenthesis"]["value"]:
    #     raise NameError(parserConst.exceptedErros[6])

    # arguments =[]
    # numbParathensis = 1
    # i = start+3
    # while i<len(tokens):
    #     arguments.append(tokens[i])
    #     if tokens[i]["type"] == constants.specialChars["closeParenthesis"]["value"]:
    #         numbParathensis-=1
    #         break
    # if numbParathensis !=0:
    #     raise NameError(parserConst.exceptedErros[0])

    return 0

tokens = tokenizer.charsToTableTokens("code.txt")
#consta = constants.symbolCloseCurlyBrace
=======
from parserHelper import *
from parserConst import parserConst
import parser

class Factory :
    def create(self, type, tokens, start):
        if type == "statementSwitch":
            return self.statementSwitch(tokens, start)
        elif type == "statementCase":
            return self.statementCase(tokens, start)

    def definedMethod(self, tokens, start):
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
    def statementSwitch(self, tokens, start):
        end = 0
        argument = searchArgs(tokens, start+1)
        if not tokens[argument["end"]+1]["type"] == "{":
            raise NameError(parser["errorMissingOpeningBrace"])
        for i in range(start, len(tokens)):
            if tokens[i]["type"] == "}":
                end = i
                foundEnd = True
                break
        if not foundEnd:
            raise NameError(parserConst["errorMissingBreakStatement"])
        return { "type" : parserConst["statementSwitch"], "argument" : argument["args"], "start" : start, "end" : end, "varType" : argument["args"][0]["type"], "AST" : parser.parser([], tokens, argument["end"]+2, end)}

    #check switch statement
    def statementCase(self, tokens, start):
        switchType = "word"
        foundEnd = False
        end = 0
        if not tokens[start+1]["type"] == switchType:
            raise NameError(parserConst["errorCaseInvalidType"]);
        for i in range(start, len(tokens)):
            if tokens[i]["type"] == "word" and tokens[i]["value"] == "break":
                end = i
                foundEnd = True
                break
        if not foundEnd:
            raise NameError(parserConst["errorMissingBreakStatement"])
        return { "type" : parserConst["statementCase"], "value" : tokens[start+1]["value"], "start" : start, "end" : end , "AST" : parser.parser([], tokens, start+2, end) }
>>>>>>> 1a89f4dc7c59784472330a03fe087e864b380a48
