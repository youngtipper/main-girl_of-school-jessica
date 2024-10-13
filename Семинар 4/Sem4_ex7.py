'''
Честно говоря, код для этой задачи писал не я, но я разобрался, что там и как работает
'''
import pandas as pd
import string
from collections import Counter

file_path = 'LICENSE.txt'
with open(file_path, 'r') as file:
    text = file.read()

translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
text = text.translate(translator).lower()

words = text.split()

word_counts = Counter(words)

most_common_words = word_counts.most_common(10)

print("Десять самых часто употребляемых слов:")
for word, count in most_common_words:
    print(f"{word}: {count}")