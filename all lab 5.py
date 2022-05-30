#NUM 1
# head = str(input("Введите названия файла\n"))
# try:
#     inf = open(head, "r")
#     num = 1
#     line = inf.readline()
#     while line != '' and num != 6:
#         print(line)
#         num += 1
#         line = inf.readline()
#     inf.close()
# except FileNotFoundError:
#     print("Неправильно введено название файла или его не существует")

#NUM 2
# head = input("Введите названия файла\n")
# inf = open(head,"r")
# line = inf.readline()
# k = 0
# try:
#     while line != "":
#         k += 1
#         line = inf.readline()
#     i = k
#     while k > i-10:
#         print(line[k])
#         k -= 1
# except FileNotFoundError:
#     print("Неправильно введено название файла или его не существует")

#NUM 3
# import fileinput
# try:
#     first = True
#     print("Введите название файлов:")
#     one = input("Первый файл:")
#     two = input("Второй файл:")
#     three = input("Введите названия фaйла в который будут залиты данные:")
#     with open(three, "wt") as out, fileinput.input(
#             files=[one,two]) as f:
#         for line in f:
#             if "next" in line:
#                 if not first:
#                     line = line.replace("next", "")
#                 else:
#                     first = False
#             out.write(line)
# except FileNotFoundError:
#     print("Неправильно введено название файла или его не существует")



# NUM 4
# file = input("Введите название файла:")
# try:
#     list = open(file, "r").read().split()
#     wm = ""
#     lm = 0
#     for w in list:
#         l = len(w)
#         if l > lm:
#            wm = w
#            lm = l
#     out_file = input("Введите название файла для вывода слова")
#     open(out_file, "w").write(wm)
# except FileNotFoundError:
#     print("Неправильно введено название файла или его не существует")

#NUM5
# import fileinput
# try:
#     first = True
#     boys = input("Введите названия фйла в который будут залиты данные:")
#     with open(boys, "wt") as out, fileinput.input(
#             files=["{}_BoysNames.txt".format(i) for i in range(1900, 2013)]) as f:
#         for line in f:
#             while line != '':
#                 line = f.readline()
#                 print(line)
#             out.write(line)
#     girls = input("Введите названия фйла в который будут залиты данные:")
#     with open(girls, "wt") as out, fileinput.input(
#             files=["{}_BoysNames.txt".format(i) for i in range(1900, 2013)]) as f:
#         for line in f:
#             while line != '':
#                 line = f.readline()
#                 print(line)
#             out.write(line)
# except FileNotFoundError:
#     print("Неправильно введено название файла или его не существует")

#NUM6
# import fileinput
# try:
#     first = True
#     boys = input("Введите названия фйла в который будут залиты данные:")
#     s = int(input("Введите начальный год"))
#     e = int(input("Введите конечный год"))
#     with open(boys, "wt") as out, fileinput.input(
#             files=["{}_BoysNames.txt".format(i) for i in range(s, e+1)]) as f:
#         for line in f:
#             while line != '':
#                 line = f.readline()
#                 print(line)
#             out.write(line)
#     girls = input("Введите названия фйла в который будут залиты данные:")
#     with open(girls, "wt") as out, fileinput.input(
#             files=["{}_BoysNames.txt".format(i) for i in range(s, e+1)]) as f:
#         for line in f:
#             while line != '':
#                 line = f.readline()
#                 print(line)
#             out.write(line)
# except FileNotFoundError:
#     print("Неправильно введено название файла или его не существует")


#NUM 7
# import re
# from collections import Counter
# head = input("Введите название файла:")
# file = open(head, 'r')
#
# f = ''
# for line in file:
#     f = f + line
#
# g = Counter(re.findall('[a-z]', f.lower()))
# for b in g:
#     print(f'{b} {g[b] / sum(g.values()):.3f}')
# file.close()

#NUM9
# a = 0
# with open('words.txt') as inp:
#     f = open('words.txt')
#     slova = (f.read().split())
# print(slova)
# for word in slova:
#     if word[0] in ['a' and 'e' and 'i' and 'o' and 'u' and 'y']:
#         print(word)
#     else:
#         pass

#NUM 8
# file = open('elements.txt', "r")
# nummer = input("Введите данные для поиска ")
# all_elements = []
# line = file.readline().split()
# while line:
#     all_elements.extend(line)
#     line = file.readline().split()
# kolvo = len(all_elements)
# while True:
#     n = 0
#     if nummer == "":
#         break
#     if nummer.isnumeric():
#         if int(nummer) > kolvo:
#             n = 1
#             print("Ошибка - число слишком большое")
#     for i in range(0, kolvo):
#         name = all_elements[i].split(",")
#         if nummer in name:
#             n = 1
#             print(*name)
#             break
#     if n == 0:
#         print("Не найдено")
#     nummer = input("Введите данные для поиска(Enter для выхода) ")