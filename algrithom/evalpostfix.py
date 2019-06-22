def postfix(input):
    """
    infix to postfix (a+b)*c-> ab+c*, a*(b+c)*d -> abc+*d*, a+b*c -> abc*+, a*(b+c*e)*d -> abce*+*d*
    a*(b*c+e)*d -> abc*e+*d*, a*(b*c+e*f)*d -> abc*ef*+*d*
    a     b  c
      * (  *
    :param input: infix
    :return: postfix
    """
    operator_dic = {}
    operator_dic['^'] = 4
    operator_dic['*'] = 3
    operator_dic['/'] = 3
    operator_dic['+'] = 2
    operator_dic['-'] = 2
    operator_dic['('] = 1
    operants = []
    operators = []

    for token in input:
        if token in "abcdefghijklmnopqrstuvwayz" or token in "0123456789":
            operants.append(token)
        elif token == "(":
            operators.append(token)
        elif token == ")":
            toptoken = operators.pop()
            while toptoken != "(":  #2 operators = [*] operant = [a,b,c,*,e,f,*,+]
                operants.append(toptoken)
                toptoken = operators.pop()
        else:
            # a * (b * c + e * f) * d -> abc * ef * + * d * , (b * c + e * f), +<* then
            if operators != []:
                if "(" in operators:  # current token is + in  (b * c + e * f)
                    lasttoken = operators.pop()  # get first * in (b * c + e * f)
                    if operator_dic[token]< operator_dic[lasttoken]:  # if +=2 < *=3
                        operants.append(lasttoken)  # operators = [*, (]

                    else:
                        operators.append(lasttoken)   # operators = [*, (, +] if (b+c*e)
                    operators.append(token)  #1 operators = [*, (, +, *] operant = [a,b,c,*,e,f]
                else:
                    if operator_dic[operators[0]]>=operator_dic[token]:
                        # a*b*c-d -> ab*c*d-
                        operants.append(operators.pop(0))
                    operators.append(token)

            else:
                operators.append(token)

    while operators != []:
        operants.append(operators.pop())

    return ''.join(operants)





def no2char(input):
    import re
    data = re.split(r'[\*\-\+/\(\)\^]', input)
    data = [x for x in data if x]
    operant = {}
    val ="abcdefghijklmnopqrstuvwayz"
    for x, y in enumerate(data):
        if y != '':
            input = re.sub(r'(?<!\d)%s(?!\d)' % y, val[x], input)
            operant[val[x]] = int(y)
    return input, operant


def evalpostfix(input, operant):
    op = []
    for x in input:
        if x in "abcdefghijklmnopqrstuvwayz":
            op.append(x)
        else:
            operator = x
            op2 = op.pop()
            op1 = op.pop()
            result = calc(operator, op1, op2, operant)
            op.append(result)
    return op[0]

def calc(operator, value1, value2, operant):

    value1 = operant.get(value1, value1)
    value2 = operant.get(value2, value2)
    if operator == '-':
        return value1-value2
    if operator == '+':
        return value1+value2
    if operator == '*':
        return value1*value2
    if operator == '/':
        return value1/value2


input = "12*(3+11*2)*13"
input, operant = no2char(input)
print(input)
print(operant)
profixvalue=postfix(input)
print(profixvalue)
print(evalpostfix(profixvalue, operant))
