import tokenizer
import scoringHelper
import parser

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
        AST = []
        AST = parser.parserFunc(AST, tokens, 0, len(tokens))
        # for node in AST:
        #     print(node)
        displayAST(AST, False, 0, len(AST))


        if(len(AST) > 0):
            # print("")
            print("score: "),
            print(scoringHelper.numberLine(AST)+1)

        # print("------------------------------")
    except Exception as e:
        print(e)

def displayAST(AST, isInnerAST, acc, end):
    currentCpt = 0
    for node in AST:
        currentCpt += 1
        if isInnerAST:
            for i in range(acc):
                print("\t"),
        print(node)
        if not node.get("AST") == None:
            if currentCpt == end:
                acc -= 1
            isInnerAST = True
            acc += 1
            print("")

            for i in range(acc):
                print("\t"),
            print("------------ subTree "+str(acc)+" -------------")
            displayAST(node["AST"], isInnerAST, acc, len(node["AST"]))

            for i in range(acc):
                print("\t"),
            print("-------------------------------------\n")
