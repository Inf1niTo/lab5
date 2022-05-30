#NUM 3
import fileinput
try:
    first = True
    print("Введите название файлов:")
    one = input("Первый файл:")
    two = input("Второй файл:")
    three = input("Введите названия фaйла в который будут залиты данные:")
    with open(three, "wt") as out, fileinput.input(
            files=[one,two]) as f:
        for line in f:
            if "next" in line:
                if not first:
                    line = line.replace("next", "")
                else:
                    first = False
            out.write(line)
except FileNotFoundError:
    print("Неправильно введено название файла или его не существует")
