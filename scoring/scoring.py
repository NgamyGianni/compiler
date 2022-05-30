from tokenizer import tokenizer
from parser import parser
from scoringHelper import *

def scoring(code):
    print("----------- Tokens -----------")

    # tokens = tokenizer.constrKeyword(code, "const")
    tokens = tokenizer.constrKeyword(code, "switch")
    # tokens = tokenizer.constrKeyword(code, "case")
    print("")
    print("".join([str(token.toString())+"\n" for token in tokens]))

    print("------------ AST -------------")
    print("")
    # tokens = [{"name" : "switch", "type" : "statementSwitch"},
    # {"name":"toto", "type":"variable"}]
    AST = parser.parser(tokens)
    if(len(AST) > 0):
        print(numberLine(AST)+1)

    print("------------------------------")
