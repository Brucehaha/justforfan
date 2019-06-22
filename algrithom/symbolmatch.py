def balancesymbol(input):
    print("input", input)
    items = []
    balance = 0
    for s in input:
        if s in ['{', '[', '(']:
            items.append(s)
        else:
            if items==[]:
                balance =0
            else:
                topsymbol = items.pop()
                if symbolmatch(topsymbol, s):
                    balance =1
                else:
                    balance = 0

    return balance

def symbolmatch(s1, s2):
    startSymbols = "({["
    closeSymbols = ")}]"
    return startSymbols.index(s1) == closeSymbols.index(s2)



print(balancesymbol("{([])})") )