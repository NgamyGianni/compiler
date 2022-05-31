from tokenizer import constants

def isSpeacialChar(t):
    for char in constants.specialChars:
        if t == constants.specialChars[char]["symbol"]:
           return True
    return False

def changeSymbolToString(code):
    for elt in constants.specialChars:
        #print(element)
        #break
        code = code.replace(
            constants.specialChars[elt]["value"], " "+constants.specialChars[elt]["symbol"]+" ")
    return code


