try:
    a = int(input('Enter first number'))
    b = int(input('Enter second number'))
    u=a/b
    print(u)
except(ZeroDivisionError):
    print('cannot divide by zero')
except(ValueError):
    print('Enter numeric values only')
    