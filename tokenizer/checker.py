from constants import specialChars

def isSpeacialChar(t):
    for char in specialChars:
        if t == specialChars[char]["value"]:
           return True, char
    return False, None

# value = isSpeacialChar("==")
