class Factory :
    def __init__(self, type, tokens, start):
        if type == "statementSwitch":
            return self.statementSwitch(tokens, start)

    def statementSwitch(self, tokens, start):
        print(tokens[start])

def variableDeclaration(tokens, start):
    """if(tokens[start+1]["type"] != constants.typeWord):
        print("rreur : nom de variable non accepté")"""
    variableName= tokens[start+1]["value"];
    return {"type": "expressionDeclaration", "variableName": variableName};

def variableAffectation(tokens, start):
    """if(tokens[start-1]["type"] != constants.typeWord):
        print("erreur : nom de variable non accepté")"""
    variableName= tokens[start-1]["value"]
    variableValue= tokens[start+1];
    return {"type": "expressionAffectation", "variableName": variableName, "variableValue": variableValue}

value = [{'type': 'word', 'value': 'const'}, {'type': 'word', 'value': '_arbre1'}, {'type': 'equal', 'value': '='}, {'type': 'word', 'value': 'a'}, {'type': 'semiColon', 'value': ';'}, {'type': 'word', 'value': 'if'}, {'type': 'openParenthese', 'value': '('}, {'type': 'word', 'value': 'a'}, {'type': 'equalSame', 'value': '=='}, {'type': 'word', 'value': 'b'}, {'type': 'closeParenthese', 'value': ')'}, {'type': 'openCrochet', 'value': '{'}, {'type': 'word', 'value': 'value'}, {'type': 'equal', 'value': '='}, {'type': 'word', 'value': '2'}, {'type': 'semiColon', 'value': ';'}, {'type': 'closeCrochet', 'value': '}'}, {'type': 'word', 'value': '_arbre1'}, {'type': 'equal', 'value': '='}, {'type': 'word', 'value': 'b'}, {'type': 'semiColon', 'value': ';'}]

value_tmp = value[:]

print(" ")
        
for i in range(len(value)):
    if value[i]["type"] == "equal":
        value_tmp[i] = variableAffectation(value, i)

L = []

for i in range(len(value)):
    if value[i]["type"] in constants.specialChars:
        L.append(i)
        print(value[i]["value"])
print(value_tmp)
print(L)
