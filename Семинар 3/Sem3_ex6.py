import numpy as np

x = input('Введите ваши иксы: ')
y = input('Введите ваши игреки: ')

x = np.array(x.split(), dtype = float)
y = np.array(y.split(), dtype = float)

k = (len(x) * np.sum(x*y) - np.sum(x) * np.sum(y)) / (len(x) * np.sum (x ** 2) - np.sum(x) ** 2)
b = (np.sum(y) - k * np.sum(x)) / len(x)

print ('y = ', k, 'x +',b)