import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''
У меня точки были не рассчитаны, поэтому я их прям тут рассчитал
'''

a = np.array([400, 340, 280, 230, 170, 120, 90, 60], dtype = float)
T = np.array([1.566, 1.537, 1.528, 1.541, 1.635, 1.814, 2.034, 2.439], dtype = float)

a2 = a**2
T2a = T**2*a

plt.figure(figsize = (4,3), dpi = 228)
plt.plot(a2, T2a, 'r^-', label='')
plt.grid()

plt.title('Зависимость T2a от a2 для физического маятника')

plt.show()