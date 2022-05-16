f = open("test.js", "r")

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