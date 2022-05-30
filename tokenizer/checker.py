from constants import specialChars

def isSpeacialChar(t):
    for char in specialChars:
        if t == specialChars[char]["value"]:
           return True
    return False

# value = isSpeacialChar("==")
