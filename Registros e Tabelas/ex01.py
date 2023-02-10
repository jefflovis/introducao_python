curso = {}
n = 3
for i in range(n):
    cod = int(input ('Digite o código do curso: '))
    while cod < 1:
        cod = int(input ('Código inválido, o código deve ser inteiro e positivo: '))
    
    nome = input ('Digite o nome do curso %d:\n' % (cod))
    area = input ('Digite a área do curso %d:\n' % (cod))
    curso [cod] = (nome, area)

print(curso)

print ('Tabela com %d cursos foi lida corretamente.' % (n))
print ('Tabela ->', curso)
cod = int(input ('Digite um código de curso para busca (<=0 para parar): '))
while codP > 0 :
    if cod in curso : # Verifica se o curso existe na tabela...
        nome, area = curso[cod] # Recupera os outros dados...
        print ('O Curso %d é %s e sua área é %s.' % (cod, nome, area))
    else:
        print ('O Curso %d não existe na tabela.' % (cod))
    codP = int(input ('Digite outro código para busca (<=0 para parar): '))
print ('Fim de Programa')