frase = str(input('Digite uma frase: ')).strip().lower()
contagem = frase.count('a')
print(f'A letra "A" aparece {contagem} vezes na frase')
primeira = frase.find('a') + 1
print(f'A primeira letra "A" aparece na posição {primeira}')
ultima = frase.rfind('a') + 1
print(f'A última letra "A" aparece na posição {ultima}')