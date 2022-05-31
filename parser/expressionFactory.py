import os
import sys
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])

from tokenizer import constants

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
        if(tokens[start+1]["type"] != constants.typeWord):
            print("erreur : nom de variable non accepté")
        variableName= tokens[start+1]["value"];
        return {"type": "expressionDeclaration", "variableName": variableName};

    def variableAffectation(self, tokens, start):
        if(tokens[start-1]["type"] != constants.typeWord):
            print("erreur : nom de variable non accepté")
        variableName= tokens[start-1]["value"]
        variableValue= tokens[start+1];
        return {"type": "expressionAffectation", "variableName": variableName, "variableValue": variableValue}

value = [{'type': 'word', 'value': 'const'}, {'type': 'word', 'value': '_arbre1'}, {'type': 'equal', 'value': '='}, {'type': 'word', 'value': 'a'}, {'type': 'semiColon', 'value': ';'}, {'type': 'word', 'value': 'if'}, {'type': 'openParenthese', 'value': '('}, {'type': 'word', 'value': 'a'}, {'type': 'equalSame', 'value': '=='}, {'type': 'word', 'value': 'b'}, {'type': 'closeParenthese', 'value': ')'}, {'type': 'openCrochet', 'value': '{'}, {'type': 'word', 'value': 'value'}, {'type': 'equal', 'value': '='}, {'type': 'word', 'value': '2'}, {'type': 'semiColon', 'value': ';'}, {'type': 'closeCrochet', 'value': '}'}, {'type': 'word', 'value': '_arbre1'}, {'type': 'equal', 'value': '='}, {'type': 'word', 'value': 'b'}, {'type': 'semiColon', 'value': ';'}]

