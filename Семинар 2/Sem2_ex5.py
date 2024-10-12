'''''В тюрьме для списков провинившиеся списки пускают по циклическому сдвигу'''''
spisok = list(map(int, input().split()))
print (spisok[1:] + spisok[:1])