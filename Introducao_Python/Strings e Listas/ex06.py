n = int(input('Tamanho: '))
while n < 1:
    n = int(input('Inválido, informe um tamanho válido: '))

v1 = [0]*n
par = [0]*n
imp = [0]*n
qp = qi = 0

for i in range (n):
    v1[i] = int(input('V1 elemento' + str(i) + ': '))
    if v1[i] % 2 == 0:
        par[qp] = v1[i]
        qp = qp + 1
    else:
        imp[qi] = v1[i]
        qi = qi + 1

    print('lidos =', v1)
    print('pares =', par)
    print('impares =', imp)