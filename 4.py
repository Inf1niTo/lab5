# NUM 4
file = input("Введите название файла:")
try:
    list = open(file, "r").read().split()
    wm = ""
    lm = 0
    for w in list:
        l = len(w)
        if l > lm:
           wm = w
           lm = l
    out_file = input("Введите название файла для вывода слова")
    open(out_file, "w").write(wm)
except FileNotFoundError:
    print("Неправильно введено название файла или его не существует")
