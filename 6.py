#NUM6
import fileinput
try:
    first = True
    boys = input("Введите названия фйла в который будут залиты данные:")
    s = int(input("Введите начальный год"))
    e = int(input("Введите конечный год"))
    with open(boys, "wt") as out, fileinput.input(
            files=["{}_BoysNames.txt".format(i) for i in range(s, e+1)]) as f:
        for line in f:
            while line != '':
                line = f.readline()
                print(line)
            out.write(line)
    girls = input("Введите названия фйла в который будут залиты данные:")
    with open(girls, "wt") as out, fileinput.input(
            files=["{}_BoysNames.txt".format(i) for i in range(s, e+1)]) as f:
        for line in f:
            while line != '':
                line = f.readline()
                print(line)
            out.write(line)
except FileNotFoundError:
    print("Неправильно введено название файла или его не существует")

