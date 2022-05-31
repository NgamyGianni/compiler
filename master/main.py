# from tokenizer import tokenizer
# from parser import parser
import scoring
import tokenizer
import parserHelper
# file = open("test.js", "r")
# code = file.read()
# scoring.scoring(code)
# file.close()

# tokens01 = tokenizer.constrKeyword(code, "const")

# print("".join([str(e.toString())+"\n" for e in consts]))
    # for const in consts:
    #     print const.toString()

# tokenizer.tokenizer(f)
# tokens = [{"name" : "switch", "type" : "statementSwitch"},
# {"name":"toto", "type":"variable"}]
# print(tokens)
# parser.parser(tokens)
# scoring.scoring(code)
if __name__=="__main__":
    print("I am the main module")
    tokens = tokenizer.charsToTableTokens("code.txt")
    print(tokens[6])
    #args = parserHelper.searchCloseCurlBrace(tokens, 6)
    args = parserHelper.searchArgs(tokens,1)
    print(args)
    # print("argument are :")
    # print(args)
    # print("last value tokens ", len(tokens))
    

