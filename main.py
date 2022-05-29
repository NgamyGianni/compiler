from tokenizer import tokenizer
from parser import parser
from scoring import scoring

file = open("test.js", "r")
code = file.read()

# consts = tokenizer.constrKeyword(s, "const")

# print("".join([str(e.toString())+"\n" for e in consts]))
    # for const in consts:
    #     print const.toString()

# tokenizer.tokenizer(f)
parser.parser()
scoring.scoring(code)

file.close()
