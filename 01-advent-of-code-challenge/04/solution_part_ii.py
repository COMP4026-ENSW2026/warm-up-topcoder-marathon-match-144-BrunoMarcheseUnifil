with open("input04.txt", encoding='utf-8', mode='r') as arquivo:
    pares = [a.replace('\n', '').split(',') for a in arquivo.readlines()]

aux = []
for p in pares:
    p[0] = p[0].split('-')
    p[1] = p[1].split('-')
    aux.append(p)

soma2 = 0
for x in aux:
    a = int(x[0][0])
    b = int(x[0][1])
    c = int(x[1][0])
    d = int(x[1][1])
    if any( [r in range(c, d+1) for r in range(a, b+1)] ):
        soma2 += 1

print(soma2)