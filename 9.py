#NUM9
a = 0
with open('words.txt') as inp:
    f = open('words.txt')
    slova = (f.read().split())
print(slova)
for word in slova:
    if word[0] in ['a' and 'e' and 'i' and 'o' and 'u' and 'y']:
        print(word)
    else:
        pass