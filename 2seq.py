spisok_cifr = input('Введите любые цифры через запятую :')
spisok_cifr = spisok_cifr.replace(';', ',').replace('/', ',').split(',')
spisok_cifr_clear = []
for i in spisok_cifr:
    spisok_cifr_clear.append(int(i))
spisok_cifr_clear = set(spisok_cifr_clear)
print(str(spisok_cifr_clear))