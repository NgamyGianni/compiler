import parserConst
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
