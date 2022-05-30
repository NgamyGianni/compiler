class Factory :
    def __init__(self, type, tokens, start):
        if type == "statementSwitch":
            return self.statementSwitch(tokens, start)

    def statementSwitch(self, tokens, start):
        print(tokens[start])
