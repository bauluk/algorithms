import cmath

def quadraticFormula(a, b, c):
    x1 = (-b + cmath.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - cmath.sqrt(b**2 - 4*a*c)) / (2*a)

    return x1, x2

print('Enter a, b, & c one at a time. Only include the number itself.')
a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))

x1, x2 = quadraticFormula(a, b, c)

print('Answers: ' + str(x1), ', ' + str(x2))
