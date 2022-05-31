from expressionFactory import Factory
from tokenizer import tokenizer
from parserHelper import *

def parser(tokens):
    AST = []
    factory = None
    for i in range(len(tokens)):
        token = tokens[i]
        if (token["type"]):
            expression = Factory(token["type"], tokens, i)
            searchArgs(tokens, i)

        if expression:
            AST.append(expression)
        else:
            AST.append(tokens[i])
    return AST
