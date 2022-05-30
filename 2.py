#NUM 2
head = input("Введите названия файла\n")
inf = open(head,"r")
line = inf.readline()
k = 0
try:
    while line != "":
        k += 1
        line = inf.readline()
    i = k
    while k > i-10:
        print(line[k])
        k -= 1
except FileNotFoundError:
    print("Неправильно введено название файла или его не существует")
