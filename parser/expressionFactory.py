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

def variableDeclaration(tokens, start):
        if(tokens[start+1]["type"] != constants.typeWord):
            print("erreur : nom de variable non accepté")
        variableName= tokens[start+1]["value"]
        return {"type": "expressionDeclaration", "variableName": variableName}

def variableAffectation(tokens, start):
        if(tokens[start-1]["type"] != constants.typeWord):
            print("erreur : nom de variable non accepté")
        variableName= tokens[start-1]["value"]
        variableValue= tokens[start+1]
        return {"type": "expressionAffectation", "variableName": variableName, "variableValue": variableValue}

tokens = [{'type': 'word', 'value': 'if'}, {'type': 'openParenthese'}, {'type': 'word', 'value': 'a'}, {'type': 'equalSame'}, {'type': 'number', 'value': '12'}, {'type': 'closeParenthese'}, {'type': 'word', 'value': ''}, {'type': 'openCurlyBrace'}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': 'var'}, {'type': 'word', 'value': 'p'}, {'type': 'equal'}, {'type': 'number', 'value': '3'}, {'type': 'semiColon'}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': 'if'}, {'type': 'openParenthese'}, {'type': 'word', 'value': 'b'}, {'type': 'equalSame'}, {'type': 'number', 'value': '3'}, {'type': 'closeParenthese'}, {'type': 'word', 'value': ''}, {'type': 'openCurlyBrace'}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': 'let'}, {'type': 'word', 'value': 'i'}, {'type': 'equal'}, {'type': 'number', 'value': '5'}, {'type': 'semiColon'}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'closeCurlyBrace'}, {'type': 'word', 'value': ''}, {'type': 'word', 'value': ''}, {'type': 'closeCurlyBrace'}, {'type': 'word', 'value': ''}]
tmp_tokens = tokens[:]
a = 0
b = 0
for i in range(len(tokens)):
    if tokens[i]["type"] == "equal":
        if tokens[i+1]["type"] != "semiColon":
            tmp_tokens[i] = variableAffectation(tokens, i)
            a+=1
        else:
            tmp_tokens[i] = variableDeclaration(tokens, i)
            b+=1
     
print(tmp_tokens)