from ast import operator
import ..tokenizer.constants as constants
import parserConst
 
class Factory :
    def __init__(self, type, tokens, start):
        if type == "statementSwitch":
            return self.statementSwitch(tokens, start)

    def statementSwitch(self, tokens, start):
        print(tokens[start])

    def definedMethod(self, tokens, start):
        if tokens[start+1]["type"] == constants.typeNumber:
            raise NameError(parserConst.exceptedErros[5])
        if tokens[start+2]["type"] != constants.specialChars["openParenthesis"]["value"]:
            raise NameError(parserConst.exceptedErros[6])

        arguments =[]
        numbParathensis = 1
        i = start+3
        while i<len(tokens):
            arguments.append(tokens[i])
            if tokens[i]["type"] == constants.specialChars["closeParenthesis"]["value"]:
                numbParathensis-=1
                break
        if numbParathensis ==0:
            raise NameError(parserConst.exceptedErros[0])


)
