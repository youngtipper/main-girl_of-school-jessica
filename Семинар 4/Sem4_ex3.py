'''
Как девочке вообще сказать, что у меня нет 5500 рублей на букет из её ирисов несчастных.
Ладно, пусть довольствуется диаграммой с долями разных видов ириса.
'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris_data.csv')

vidy_etogo_neschastnogo_irisa = df['Species'].value_counts(normalize=True)

mikrolepestok = (df['PetalLengthCm'] > 1.2).mean()
normislepestok = ((df['PetalLengthCm'] > 1.2) & (df['PetalLengthCm'] < 1.5)).mean()
ultralepestok = (df['PetalLengthCm'] > 1.5).mean()

fig, axs = plt.subplots(1, 2, figsize=(12, 12))


axs[0].pie(vidy_etogo_neschastnogo_irisa, labels=vidy_etogo_neschastnogo_irisa.index) # Диаграмма для доли разных видов ирисов
axs[0].set_title('ариш вот столько ирисов, которые я пока не могу тебе купить')


axs[1].pie([mikrolepestok, normislepestok, ultralepestok], labels=['до 1.2 см (поясните за маленьковость)', '1.35 +- 0.15 см', 'больше 1.5см (зачем он такой большой нужен)']) # Диаграмма для доли ирисов с разной длиной лепестка
axs[1].set_title('а вот их длина')

plt.tight_layout()
plt.show()
