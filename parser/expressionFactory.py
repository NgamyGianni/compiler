class Factory :
    def __init__(self, type, token, start):
        if type == "statementSwitch":
            return statementSwitch(token, start)

    def statementSwitch(token, start):
        print('switch')
