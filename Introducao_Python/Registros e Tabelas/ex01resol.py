curso = {}
n = 1 #len(curso)
cod = int(input ('Digite o código do curso %d: ' %(n)))

while cod > 0:
    nome = input ('Digite o nome do curso %d:\n' % (cod))
    area = input ('Digite a área do curso %d:\n' % (cod))
    curso [cod] = (nome, area)
    n = n+1
    cod = int(input ('Digite o código do curso %d: ' %(n)))

    while cod < 1 :
        cod = int(input ('Código inválido, o código deve ser inteiro e positivo: '))
    
    

print(curso)

print ('Tabela com %d cursos foi lida corretamente.' % (n))
print ('Tabela ->', curso)
cod = int(input ('Digite um código de curso para busca (<=0 para parar): '))
while cod > 0 :
    if cod in curso : # Verifica se o curso existe na tabela...
        nome, area = curso[cod] # Recupera os outros dados...
        print ('O Curso %d é %s e sua área é %s.' % (cod, nome, area))
    else:
        print ('O Curso %d não existe na tabela.' % (cod))
    cod = int(input ('Digite outro código para busca (<=0 para parar): '))
print ('Fim de Programa')