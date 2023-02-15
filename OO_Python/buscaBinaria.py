def busca_binaria(lista, low, high, elemento):
    if high >= low:
        meio = (high + low) // 2
        # se for o elemento que estamos procurando, retorne meio
        if lista[meio] == elemento:
            return meio
        elif lista[meio] > elemento:
            return busca_binaria(lista, low, meio-1, elemento)
        elif lista[meio] < elemento:
            return busca_binaria(lista, high, meio+1, elemento)
    else:
        return -1
    
l = [2, 5, 20, 50, 120]
x = 120

print(busca_binaria(l,2,120,x))

