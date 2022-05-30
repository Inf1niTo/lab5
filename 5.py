#NUM5
import fileinput
try:
    first = True
    boys = input("Введите названия фйла в который будут залиты данные:")
    with open(boys, "wt") as out, fileinput.input(
            files=["{}_BoysNames.txt".format(i) for i in range(1900, 2013)]) as f:
        for line in f:
            while line != '':
                line = f.readline()
                print(line)
            out.write(line)
    girls = input("Введите названия фйла в который будут залиты данные:")
    with open(girls, "wt") as out, fileinput.input(
            files=["{}_BoysNames.txt".format(i) for i in range(1900, 2013)]) as f:
        for line in f:
            while line != '':
                line = f.readline()
                print(line)
            out.write(line)
except FileNotFoundError:
    print("Неправильно введено название файла или его не существует")
