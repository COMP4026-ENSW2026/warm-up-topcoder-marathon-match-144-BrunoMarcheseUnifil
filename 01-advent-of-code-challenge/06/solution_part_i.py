with open("input06.txt", encoding='utf-8', mode='r') as arquivo:
    linha = arquivo.readline().strip()

for i in range(len(linha)):
    if len(set(linha[i:i+4]))==4:
        print(i+4)
        break