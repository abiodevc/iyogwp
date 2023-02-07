b = 0
c = 0

def contagem(a,b,c):
    soma = True
    if a == 59:
        a = 0
        b += 1
        soma = False
    if b == 59 and a == 59:
        b = 0
        c += 1
    elif soma:
        a = a + 1
    return a
a = 0
i = 0
while i < 100:
    a = contagem(a,b,c)
    print(a)
    i+=1