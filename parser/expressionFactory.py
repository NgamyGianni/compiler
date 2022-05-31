class Factory :
    def __init__(self, type, tokens, start):
        if type == "statementSwitch":
            return self.statementSwitch(tokens, start)
        
        if type == "variableDeclaration":
            return self.variableDeclaration(tokens, start)
        
        if type == "variableAffectation":
            return self.variableAffectation(tokens, start)

    def statementSwitch(self, tokens, start):
        print(tokens[start])
        
    def variableDeclaration(self, tokens, start):
        variableName= tokens[start+1]["value"];
        return {"type": "expressionDeclaration", "variableName": variableName}

    def variableAffectation(self, tokens, start):
        variableName= tokens[start-1]["value"]
        variableValue= tokens[start+1];
        return {"type": "expressionAffectation", "variableName": variableName, "variableValue": variableValue}
