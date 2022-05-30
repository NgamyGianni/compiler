import re
specialChars = {
    'operatorPlus': {'symbol': 'plus', 'value': "+"},
    'operatorMinus': {'symbol': 'minus', 'value': "-"},
    'operatorMultiply': {'symbol': 'mult', 'value': "*"},
    'operatorDivide': {'symbol': 'divide', 'value': "/"},
    'operatorEqual': {'symbol': 'equal', 'value': "="},
    'compEqual': {'symbol': 'equalSame', 'value': "=="},
    'compGreaterThan': {'symbol': 'greaterThan', 'value': ">="},
    'compGreater': {'symbol': 'great', 'value': ">"},
    'compLowerThan': {'symbol': 'lowerThan', 'value': "<="},
    'compLower': {'symbol': 'lower', 'value': "<"},
}

symbolCompEqual = "equal"
symbolCompGreaterThan = "greaterThan"
symbolComptGreater = "great"
symbolCompLowerThan = "lowerThan"
symbolCompLower = "lower"

typeNumber = "number"
typeWord = "word"
