# from expressionFactory import Factory
import expressionFactory as factory
from tokenizer import tokenizer
from parserHelper import *
from parserConst import parserConst

def parser(AST, tokens, start, end):
    # factory = Factory();
    # AST = []
    i = start
    while i >= start and i  < end:
    # for i in range(len(tokens)):
        expression = None
        token = tokens[i]
        if (token["type"] == "word" and token["value"] == "switch"):
            expression = factory.create(parserConst["statementSwitch"], tokens, i)
        elif token["type"] == "word" and token["value"] == "case":
            expression = factory.create(parserConst["statementCase"], tokens, i)

        if expression:
            AST.append(expression)
            i = expression["end"] + 1
        else:
            AST.append(tokens[i])
        i += 1
    return AST
