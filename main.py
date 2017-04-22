import re


def operation(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    else:
        try:
            return a / b
        except:
            return "Error"


def priority(operator, operators, numbers):
    if len(operators) == 0:
        operators.append(operator)
    else:
        if operators[len(operators) - 1] == '/' or operators[len(operators) - 1] == '*':
            b = numbers.pop()
            a = numbers.pop()
            aux = operators.pop()
            numbers.append(operation(a, b, aux))
            priority(operator, operators, numbers)
        elif (operators[len(operators) - 1] == '+' or operators[len(operators) - 1] == '-') and (
                operator == '+' or operator == '-'):
            b = numbers.pop()
            a = numbers.pop()
            aux = operators.pop()
            numbers.append(operation(a, b, aux))
            priority(operator, operators, numbers)
        elif (operators[len(operators) - 1] == '+' or operators[len(operators) - 1] == '-') and (
                operator == '/' or operator == '*'):
            operators.append(operator)


def shuntingYard(expression):
    operators = []
    numbers = []
    expression = expression.split()

    for x in expression:
        if re.match(r'^[\+\-\*\/]$', x):
            if len(operators) == 0:
                operators.append(x)
            else:
                priority(x, operators, numbers)
        else:
            numbers.append(float(x))

    while (len(operators) != 0):
        b = numbers.pop()
        a = numbers.pop()
        operator = operators.pop()

        aux = operation(a, b, operator)

        if aux == "Error":
            return aux
        else:
            numbers.append(aux)

    return numbers.pop()


def checkingInput(expression):
    if re.match(r'^([0-9]+[ ]*[\+\-\*\/][ ]*)+[0-9]+$', expression):
        try:
            print("%.2f" % shuntingYard(expression))
        except:
            print("Error")
    else:
        print("Error")


expression = input()
expression = expression.replace("+", " + ")
expression = expression.replace("-", " - ")
expression = expression.replace("*", " * ")
expression = expression.replace("/", " / ")

checkingInput(expression)

