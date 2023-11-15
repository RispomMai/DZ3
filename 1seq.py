count_spisok = int(input('Введите количество элементов: '))
spisok_bukv = []
for i in range(0,count_spisok):
    print('Введите',i,' элемент')
    spisok_bukv.append(int(input()))
    spisok_bukv.sort()
print(str(spisok_bukv))