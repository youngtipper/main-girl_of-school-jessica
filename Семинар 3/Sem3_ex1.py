n = int(input('Введите какое-нибудь целое и неотрицательное n = '))
def bibonacci(n):
    if n == 0:
        return n
    if n == 1:
        return n
    else:
        return bibonacci(n - 2) + bibonacci(n - 1)
print ('Вам приз! В подарок вашей королевской особе n-число Фибоначчи: ', bibonacci(n))