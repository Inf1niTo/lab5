#NUM 8
file = open('elements.txt', "r")
nummer = input("Введите данные для поиска ")
all_elements = []
line = file.readline().split()
while line:
    all_elements.extend(line)
    line = file.readline().split()
kolvo = len(all_elements)
while True:
    n = 0
    if nummer == "":
        break
    if nummer.isnumeric():
        if int(nummer) > kolvo:
            n = 1
            print("Ошибка - число слишком большое")
    for i in range(0, kolvo):
        name = all_elements[i].split(",")
        if nummer in name:
            n = 1
            print(*name)
            break
    if n == 0:
        print("Не найдено")
    nummer = input("Введите данные для поиска(Enter для выхода) ")