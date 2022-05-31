from tokenizer.constants import specialChars

def isSpeacialChar(t):
    for char in specialChars:
        if t == specialChars[char]["symbol"]:
           return True
    return False

def changeSymbolToString(code):
    for elt in specialChars:
        #print(element)
        #break
        code = code.replace(
            specialChars[elt]["value"], " "+specialChars[elt]["symbol"]+" ")
    return code


