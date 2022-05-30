class Factory :
<<<<<<< HEAD
    def __init__(self, type, tokens, start):
        if type == "statementSwitch":
            return self.statementSwitch(tokens, start)

    def statementSwitch(self, tokens, start):
        print(tokens[start])
=======
    def __init__(self, type, token, start):
        if type == "statementSwitch":
            return statementSwitch(token, start)

    def statementSwitch(token, start):
        print('switch')
>>>>>>> bcd52b3dd8485ea1c89da4a61fe3726b5d1f1618
