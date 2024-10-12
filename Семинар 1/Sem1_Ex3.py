numbers = list(map(int, input('Давайте сюда ваши числа: ').split()))
n = 1
for i in numbers:
    n = i*n
print ('Держите ваше среднее геометрическое: ', (n)**(1/len(numbers)))
