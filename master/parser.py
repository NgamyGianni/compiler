import expressionFactory as factory
import tokenizer
import parserConst

def parserFunc(AST, tokens, start, end):

    # AST = []
    i = start
    while i >= start and i  < end:
    # for i in range(len(tokens)):
        expression = None
        token = tokens[i]
        if (token["type"] == "word" and token["value"] == "switch"):
            expression = factory.create(parserConst.statementSwitch, tokens, i)
        elif token["type"] == "word" and token["value"] == "case":
            expression = factory.create(parserConst.statementCase, tokens, i)
        elif token["type"] == "word" and token["value"] == parserConst.declarationFunction:
            expression = factory.create(
                parserConst.declarationFunction, tokens, i)
        if expression:
            AST.append(expression)
            i = expression["end"] 
        else:
            AST.append(tokens[i])
        i += 1
    return AST
