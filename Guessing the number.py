import random
class ValueTooSmallError(Exception):
    pass
class ValueTooLargeError(Exception):
    pass
n1=random.randint(0,9)
print(n1)
while(True):

    try:
        n2=int(input('Enter the number :'))
        if n2<n1:
            raise ValueTooSmallError
        elif n2>n1:
            raise ValueTooLargeError
        break
    except(ValueTooSmallError):
        print('Too Small')
    except(ValueTooLargeError):
        print('Too Large')
print('You guess it correctly')
