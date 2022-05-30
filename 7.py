#NUM 7
import re
from collections import Counter
head = input("Введите название файла:")
file = open(head, 'r')

f = ''
for line in file:
    f = f + line

g = Counter(re.findall('[a-z]', f.lower()))
for b in g:
    print(f'{b} {g[b] / sum(g.values()):.3f}')
file.close()
