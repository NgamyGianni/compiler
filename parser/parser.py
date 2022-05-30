from expressionFactory import Factory
from tokenizer import tokenizer

def parser(tokens):
    print("code in parser")
    AST = []
    factory = None
    for i in range(len(tokens)):
        token = tokens[i]
        if (token["type"]):
            print("parsing: blabla");
            factory = Factory(token["type"], tokens, i)
    AST.append(factory)
    return AST
