from expressionFactory import Factory
from tokenizer import tokenizer

class Factory :
    def __init__(self, type, token, start):
        if type == "statementSwitch":
            return self.statementSwitch(token)

    def statementSwitch(token, start):
        print('switch')

def parser(tokens):
    print("code in parser")
    AST = []
<<<<<<< HEAD
    factory = None
=======
>>>>>>> bcd52b3dd8485ea1c89da4a61fe3726b5d1f1618
    for i in range(len(tokens)):
        token = tokens[i]
        if (token["type"]):
            print("parsing: blabla");
<<<<<<< HEAD
            factory = Factory(token["type"], tokens, i)
    AST.append(factory)
    return AST
=======
            Factory(token["type"], token, i)
>>>>>>> bcd52b3dd8485ea1c89da4a61fe3726b5d1f1618
