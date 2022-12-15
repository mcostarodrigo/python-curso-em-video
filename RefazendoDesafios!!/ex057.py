s = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0] #O [0] no final faz o fatiamneto da str, pegando apenas o primeiro termo.
while s != 'M' and s != 'F': #Outro forma de escrever seria "while s not in 'MmFf':"
        s = input('Dados inválidos. Por favor, informe seu sexo: ').upper().strip()[0] #O[0] no final faz o fatiamneto da str, pegando apenas o primeiro termo.
print(f'Sexo {s} registrado com sucesso')

