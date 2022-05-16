from tokenizer import tokenizer
from parser import parser
from scoring import scoring

f = open("test.js", "r")
s = f.read()

consts = tokenizer.constrKeyword(s, "const")

print([e.toString() for e in consts])

f.close()
# tokenizer.tokenizer(f)
parser.parser()
scoring.scoring()
