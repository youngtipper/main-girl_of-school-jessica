'''''
Приходит мужик на шоу талантов: я, говорит, любое сообщение
могу разбить на группы и в обратном порядке их прочитать.
Ему говорят: скажи наоборот "в недрах тундры выдры в гетрах тырят в ведра ядра кедров"
У мужика отвалилась жопа
'''''
input_data = input().split()
G = int(input_data[0]) 
s = input_data[1]
length = len(s)
group_size = length // G
result = ""
for i in range(G):
    group = s[i * group_size:(i + 1) * group_size]
    result += group[::-1]

print(result)