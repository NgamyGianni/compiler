from expressionFactory import Factory
from tokenizer import tokenizer
from parserHelper import *

def parser(tokens):
    AST = []
    factory = None
    for i in range(len(tokens)):
        token = tokens[i]
        if (token["type"]):
            factory = Factory(token["type"], tokens, i)
            #deplace dans scoring
            try:
                searchArgs(tokens, i)
            except Exception as e:
                print(e)

    AST.append(factory)
    return AST
