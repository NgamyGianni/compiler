from expressionFactory import Factory
from tokenizer import tokenizer
from parserHelper import *
from parserConst import parserConst

def parser(tokens, start, end):
    factory = Factory();
    AST = []
    i = 0
    while i  < len(tokens):
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
