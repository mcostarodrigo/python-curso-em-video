media = 0
maior = 0
maisvelho = ''
totmulher = 0
for p in range(1, 5):
    print(5 * '-', f'{p}º PESSOA', 5*'-')
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    media = idade + media
    sexo = input('[M/F]: ').strip()
    if p == 1 and sexo in 'Mm':
        maior = idade
    if idade > maior and sexo in 'Mm':
        maior = idade
    if sexo in 'Mm' and maior == idade:
        maisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
print(f'A média de idade do grupo é de {media / 4} anos\nO homem mais velho tem {maior}, e seu nome é {maisvelho}')
print(f'Ao todo são {totmulher} mulheres com menos de 20 anos ')
