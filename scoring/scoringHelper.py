def numberLine(ast):
    if len(ast) < 80:
        return 5;
    elif len(ast) < 100:
        return 3;
    elif len(ast) < 200:
        return 1;
    else:
        return 0;
