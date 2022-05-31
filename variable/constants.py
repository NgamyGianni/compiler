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
    'quotationMark': {'symbol': 'quotationMark', 'value': '""'},
    'openParenthesis': {'symbol': 'openParenthese', 'value': "("},
    'closeParenthesis': {'symbol': 'closeParenthese', 'value': ")"},
    'openCrochet': {'symbol': 'openCrochet', 'value': "{"},
    'closeCrochet': {'symbol': 'closeCrochet', 'value': "}"},
    'point': {'symbol': 'point', 'value': "."},
    'semiColon': {'symbol': 'semiColon', 'value': ";"}
}

typeVariable= 'variable'
typeString= 'string'

typeNumber = "number"
typeWord = "word"

expressionDeclaration= "variableDeclaration"
expressionAffectation= "variableAffectation"
expressionMethodCall= "objectMethodCall"

declarationVariable = ["var", "let", "const"]

errorMissingOpenParenthesis = "Error: missing a open parenthesis"
errorMissingCloseParenthesis= "Error: missing a close parenthesis"
errorMissingQuotationMark= "Error: missing quotation mark"
errorMissingWord= "Error: missing a word for valid expression"
