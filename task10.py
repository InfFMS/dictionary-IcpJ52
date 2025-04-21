# Нужно считать файл parameters.txt. 
# Это файл с настройками расчетной модели.
# Формат в файле следующий первое слово в строке - это ключ, 
# потом после пробела - значение (может быть строкой, числом, или набором чисел),
# все, что после символа "//" это комментарий должно игнорироваться.
# Реализуйте считывание значений из файла и запись этих значений в словарь.
with open('parameters.txt') as f:
    dct = dict()
    for line in f.readlines():
        if '//' in line:
            line = line[:line.find('//')]
        line1 = line[:line.find(' ')]
        line2 = line[line.find(' ') + 1:]
        line1 = line1.replace('\t', '')
        line1 = line1.replace('\n', '')
        line2 = line2.replace('\t', '')
        line2 = line2.replace('\n', '')
        if len(line1) > 0:
            dct[line1] = line2
    print(dct)
