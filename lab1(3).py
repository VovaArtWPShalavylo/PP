num1 = int(input('Enter fist number'))
num2 = int(input('Enter second number'))

def func(num1,num2):
    if num1 < 0:
        raise Exception("Введіть додатнє число")
    if num2 < 0:
        raise Exception("Введіть додатнє число")

    res = bool(0)
    if num1 % num2 == 0:
        res = bool(1)
        return (res)
    else:
        return (res)


print(func(num1, num2))
