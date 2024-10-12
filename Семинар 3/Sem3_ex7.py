import numpy as np

n = int(input ('Введите количество строк: '))
m = int(input ('Введите количество столбцов: '))

matrix = np.zeros((n,m))

for i in range (n):
    for j in range (m):
        matrix[i][j] = float(input(f"Введите {j+1} элемент {i+1} строки: "))

svobodnyy_chlen = matrix[:, -1]
zapertye_chlens = matrix[:, :-1]

try:
    matrix_poreshali = np.linalg.solve(zapertye_chlens,svobodnyy_chlen)
except np.linalg.LinAlgError as e:
    matrix_poreshali = 'Братанчик систему кривую ввел, давай еще разок попробуем'

print(matrix_poreshali)