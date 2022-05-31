from constants import specialChars

def isSpeacialChar(t):
    for char in specialChars:
        #print(specialChars[char]["value"])
        if t == specialChars[char]["value"]:
           return True, char
    return False, None

#value = isSpeacialChar("==")
