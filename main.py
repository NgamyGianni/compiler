from tokenizer import tokenizer
from parser import parser
from scoring import scoring

f = open("test.js", "r")
tokenizer.tokenizer(f)
parser.parser()
scoring.scoring()
