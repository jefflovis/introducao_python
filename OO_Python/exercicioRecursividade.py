# solução do professor para recursividade
def is_crescente(lista):
    if len(lista)<=1:
        return True
    else:
        return lista[0]<=lista[1] and is_crescente(lista[1:])

lista1 = [1,2,3,4,5]
lista2 = [1,2,3,5,6,4]
lista3 = [12,17,52,59,68,123]

print(is_crescente(lista1))
print(is_crescente(lista2))
print(is_crescente(lista3))

# O que acontece na função
# 1 <= 2 ^ asc (2,3,4,5)
# True 2 <= 3 ^ asc (3,4,5)
# True ^ True ^ 3 <= 4 ^ asc (4,5)
# True ^ True ^ True 4 <= 5 ^ asc (5)
# True ^ True ^ True ^ True # Retornando caso base [5]