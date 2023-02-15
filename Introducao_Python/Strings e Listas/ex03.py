nome1 = input('Irforme a primeira palavra:')
nome2 = input('Irforme a segunda palavra:')
qtd = 0
#tem = int(nome1 in nome2)
#print(tem)
for i in range(len(nome1)):    
    pos=nome1.find(nome2)
    if pos != -1:
        qtd = qtd + 1

print(qtd)

# Resolução do professor

proc = input('Irforme a primeira palavra:')
texto = input('Irforme a segunda palavra:')

cont = 0

pos = texto.find(proc)

while pos != -1:
    cont = cont + 1
    pos = texto.find(proc, pos + 1)
print(cont)

