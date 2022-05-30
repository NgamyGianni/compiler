from tokenizer import tokenizer
from parser import parser
from scoringHelper import *

def scoring(code):
    try:
        print("----------- Tokens -----------")

        code = "test.js"
        tokens = tokenizer.charsToTableTokens(code)
        print("")
        for token in tokens:
            print(token)
        # print("".join([str(token.toString())+"\n" for token in tokens]))

        print("")
        print("------------ AST -------------")
        print("")
        # tokens = [{"name" : "switch", "type" : "statementSwitch"},
        # {"name":"toto", "type":"variable"}]
        AST = parser.parser(tokens)
        if(len(AST) > 0):
            print(numberLine(AST)+1)

        print("------------------------------")
    except Exception as e:
        print(e)
