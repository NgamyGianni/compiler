f = open("test.js", "r")

specialChars = {
    'newLine' : {'regRule' : '/\r\n/g', 'value' :'\n'},
    'case' : {'regRule' : '/case/g', 'value' :'case'},
    # endInstruct:    {regRule: /;/g,  value:';'},
    # equal:          {regRule: /=/g, value:'='},
    # point:           {regRule: /\./g, value:'.'},
    # virgule:           {regRule: /\,/g, value:','},
    # quotationMark:  {regRule: /\"/g, value:'"'},
    # openParenthese:  {regRule: /\(/g, value:'"'},
    # closeParenthese:  {regRule: /\)/g, value:'"'}
}

def hello():
    print("yoyoyo")
    print(specialChars['case']['regRule'])

hello()

keys = ["await", "break", "case", "catch", "class", "const", "continue", "debugger", "default",
        "delete", "do", "else", "enum", "export", "extends", "false", "finally", "for", "function",
        "if", "implements", "import", "in", "instanceof", "interface", "let", "new", "null", "package",
        "private", "protected", "public", "return", "super", "switch", "static", "this", "throw", "try",
        "true", "typeof", "var", "void", "while", "with", "yield"]
L = []

Lines = f.readlines()

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))

def checkifInstruction(code):
    print(L)

for sentence in f.read().split("\n"):
    for word in sentence.split(" "):
        if word in keys:
            if(word=="if"):
                L.append(word)
                checkifInstruction(word)
