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
    for i in range(len(tokens)):
        token = tokens[i]
        if (token["type"]):
            print("parsing: blabla");
            Factory(token["type"], token, i)
