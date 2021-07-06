def math():
    mathi = int(input('What math?\nAdd(1)\nSubtract(2)\nMultiply(3)\nDivide(4)\nPoop(5)\n'))
    if mathi == 1:
        print('Addition')
        n1 = int(input('first number?'))
        n2 = int(input('second number'))
        print(n1 + n2)
    if mathi == 2:
        print('Subtraction')
        n1 = int(input('first number?'))
        n2 = int(input('second number'))
        print(n1 - n2)
    if mathi == 3:
        print('Multiplication')
        n1 = int(input('first number?'))
        n2 = int(input('second number'))
        print(n1 * n2)
    if mathi == 4:
        print('Division')
        n1 = int(input('first number?'))
        n2 = int(input('second number'))
        print(n1 / n2)
    if mathi == 5:
        inw = input('What Were you thinking that would do?')
        print('I do not know What"' + inw + '"means')
    if mathi == 'q':
        quit()