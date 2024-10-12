# https://youtube.com/watch?v=onD9sOEejzs&feature=shared
s = input()
regular_palindrome = s == s[::-1]
brat_perevertysh = {'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', '1': '1', '8': '8',
    'E': '3', 'J': 'L', 'S': '2', 'Z': '5', '3': 'E', '2': 'S', '5': 'Z', 'L': 'J'}
palindrom_mordnilap = True
for i in s:
    if i not in brat_perevertysh:
        palindrom_mordnilap = False
        break
mirror_string = True
for i in range(len(s)):
    if s[i] != brat_perevertysh.get(s[i], None):
        mirror_string = False
        break
if not palindrom_mordnilap and not regular_palindrome:
    result = f'"{s} - не палиндром ты мне, прямолинейный дурачина."'
elif regular_palindrome and not palindrom_mordnilap:
    result = f'"{s} - обычный палиндромчик со скромной зарплатой и комнатой в коммуналке."'
elif palindrom_mordnilap and not mirror_string:
    result = f'"{s} - палиндром со средним доходом, в зеркале очень похож сам на себя."'
elif regular_palindrome and palindrom_mordnilap and mirror_string:
    result = f'"{s} - богатый палиндром, в зеркале абсолютно идентичен сам себе, мало таких на Руси осталось."'
else:
    result = f'"{s} - не палиндром, ему явно не хватает зеркальности. Но ничего, еще вся жизнь впереди."'

print(result)