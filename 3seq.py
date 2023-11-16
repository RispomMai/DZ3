spisok_cifr = set(input('Введите любые цифры первого множества через запятую :'))
spisok_cifr_new = set(input('Введите блюые цифры второго множества через запятую :'))
spisok_cifr.difference_update(spisok_cifr_new)
print(spisok_cifr)