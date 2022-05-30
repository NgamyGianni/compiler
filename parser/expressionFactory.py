from parserHelper import *
from parserConst import parserConst
import parser

class Factory :
    def create(self, type, tokens, start):
        if type == "statementSwitch":
            return self.statementSwitch(tokens, start)
        elif type == "statementCase":
            return self.statementCase(tokens, start)

    #check switch statement
    def statementSwitch(self, tokens, start):
        argument = searchArgs(tokens, start+1)
        if not tokens[argument["end"]+1]["type"] == "{":
            raise NameError(parser["errorMissingOpeningBrace"])
        return { "type" : parserConst["statementSwitch"], "argument" : argument["args"], "start" : start, "end" : argument["end"], "varType" : argument["args"][0]["type"] }

    #check switch statement
    def statementCase(self, tokens, start):
        switchType = "word"
        foundEnd = False
        end = 0
        if not tokens[start+1]["type"] == switchType:
            raise NameError(parserConst["errorCaseInvalidType"]);
        for i in range(start, len(tokens)):
            if tokens[i]["type"] == "word" and tokens[i]["value"] == "break":
                end = i
                foundEnd = True
                break
        if not foundEnd:
            raise NameError(parserConst["errorMissingBreakStatement"])
        return { "type" : parserConst["statementCase"], "value" : tokens[start+1]["value"], "start" : start, "end" : end , "node" : parser.parser(tokens, start+1, end) }
