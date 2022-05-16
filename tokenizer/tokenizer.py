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
tokens = []

def hello():
    print("yoyoyo")
    print(specialChars['case']['regRule'])

# keys = ["await", "break", "case", "catch", "class", "const", "continue", "debugger", "default",
#         "delete", "do", "else", "enum", "export", "extends", "false", "finally", "for", "function",
#         "if", "implements", "import", "in", "instanceof", "interface", "let", "new", "null", "package",
#         "private", "protected", "public", "return", "super", "switch", "static", "this", "throw", "try",
#         "true", "typeof", "var", "void", "while", "with", "yield"]

def displayFileLines(f):
    Lines = f.readlines()
    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        print("Line{}: {}".format(count, line.strip()))

# def checkifInstruction(code):
#     print(L)

def tokenizer(file):
    # for sentence in f.read().split("\n"):
    Lines = file.readlines()
    for line in Lines:
        for word in line.split(" "):
            tokens.append({"type" : "word", "value" : word})
            # checkifInstruction(word)
    for token in tokens:
        print(token)

class constant :

    def __init__(self, name, value):
        self.name = name
        self.value = value

        if '"'in value:
            self.type = "string"
        else:
            if '.' in value:
                self.type = "float"
            else:
                self.type = "int"

        self.struct = {"name" : self.name, "value" : self.value, "type" : self.type}

    def toString(self):
        return self.struct

def stringToLines(s):
    return [word.split(" ") for word in s.split("\n")]

def linesToLine(lines):
    return [word for line in lines for word in line]

def lineToList(line, index):
    return ''.join(line[index:])

def checkKeyword(keyword, s):
    lines = stringToLines(s)
    return keyword in linesToLine(lines)

def verifyLine(keyword, line):
    return len(line) >= 4 and line[0] == keyword and line[2] == "=" and ";" in lineToList(line, 2)

def constrKeyword(s, keyword):
    return [constant(line[1], line[3].split(";")[0]) for line in stringToLines(s) if keyword in line]
