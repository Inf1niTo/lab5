#NUM 1
head = str(input("Введите названия файла\n"))
try:
    inf = open(head, "r")
    num = 1
    line = inf.readline()
    while line != '' and num != 6:
        print(line)
        num += 1
        line = inf.readline()
    inf.close()
except FileNotFoundError:
    print("Неправильно введено название файла или его не существует")
