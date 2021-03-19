from stack import Stack


def infixtopostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opstack = Stack()
    postfixlist = []
    tokenlist = infixexpr.split()

    for token in tokenlist:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixlist.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            toptoken = opstack.pop()
            while toptoken != '(':
                postfixlist.append(toptoken)
                toptoken = opstack.pop()
        else:
            while (not opstack.isempty()) and \
               (prec[opstack.peek()] >= prec[token]):
                    oper = opstack.pop()
                    postfixlist.append(oper)
            opstack.push(token)

    while not opstack.isempty():
        postfixlist.append(opstack.pop())
    return " ".join(postfixlist)


print(infixtopostfix("( A + B ) * C + D"))
