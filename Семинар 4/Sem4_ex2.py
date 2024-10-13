'''
Повторение одно и того же действия раз за разом в надежде на изменение - это безумие
(но когда я снова дотянул с домашкой по информатике до последнего - это случайность)
'''
import numpy as np
import matplotlib.pyplot as plt

normis_malenkiy = np.random.normal(loc = 52, scale = 13, size = 50)
plt.subplot(2,3,1)
plt.hist(normis_malenkiy,10 )

normis_sredniy = np.random.normal(loc = 52, scale = 13, size = 5000)
plt.subplot(2,3,5)
plt.hist(normis_sredniy, 50)

normis_bolshoy = np.random.normal(loc = 0, scale = 10, size = 500000)
plt.subplot(2,3,3)
plt.hist(normis_bolshoy, 100)
plt.show()

