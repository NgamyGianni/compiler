from tokenizer import tokenizer

def scoring(code):
    print("----------- Tokens -----------")

    # tokens = tokenizer.constrKeyword(code, "const")
    tokens = tokenizer.constrKeyword(code, "switch")
    # tokens = tokenizer.constrKeyword(code, "case")
    print("")
    print("".join([str(token.toString())+"\n" for token in tokens]))

    print("------------ AST -------------")
    print("")

    print("------------------------------")
