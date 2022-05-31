import re

specialChars = {
    'operatorPlus': {'symbol': 'plus', 'value': "+"},
    'operatorMinus': {'symbol': 'minus', 'value': "-"},
    'operatorMultiply': {'symbol': 'mult', 'value': "*"},
    'operatorDivide': {'symbol': 'divide', 'value': "/"},
    'compEqual': {'symbol': 'equalSame', 'value': "=="},
    'operatorEqual': {'symbol': 'equal', 'value': "="},
    'compGreaterThan': {'symbol': 'greaterThan', 'value': ">="},
    'compGreater': {'symbol': 'great', 'value': ">"},
    'compLowerThan': {'symbol': 'lowerThan', 'value': "<="},
    'compLower': {'symbol': 'lower', 'value': "<"},
    'opAnd': {'symbol': 'and', 'value': "&&"},
    'opOr': {'symbol': 'or', 'value': "||"},
    'quotationMark': {'symbol': 'quotationMark', 'value': '""'},
    'openParenthesis': {'symbol': 'openParenthesis', 'value': "("},
    'closeParenthesis': {'symbol': 'closeParenthesis', 'value': ")"},
    'openCurlyBrace': {'symbol': 'openCurlyBrace', 'value': "{"},
    'closeCurlyBrace': {'symbol': 'closeCurlyBrace', 'value': "}"},
    'point': {'symbol': 'point', 'value': "."},
    'semiColon': {'symbol': 'semiColon', 'value': ";"}
}
symbolPlus = "plus"
symbolMinus = "minus"
symbolMultiply = "multiply"
symbolDivide = "divide"
symbolCompLower = "lower"
symbolCompEqual = "equal"
symbolEqualSame = "equalSame"
symbolCompGreaterThan = "greaterThan"
symbolComptGreater = "great"
symbolCompLowerThan = "lowerThan"
symbolCompLower = "lower"
symbolAnd = "and"
symbolOr = "or"
symbolQuotationMark = "quotationMark"
symbolOpenParenthesis = "openParenthesis"
symbolCloseParenthesis = "closeParenthesis"
symbolOpenCurlyBrace = "openCurlyBrace"
symbolCloseCurlyBrace = "closeCurlyBrace"
symbolPoint = "point"
symbolSemiColon = "semiColon"
typeNumber = "number"
typeWord = "word"

# if __name__=="__main__":
#     print("I am in constant module")