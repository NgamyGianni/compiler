from tokenizer import tokenizer

def parser(tokens):
    print("code in parser")
    for token in tokens:
        switch(token.type){
         case "blabl":
            print("parsing: blalbla");
        }
