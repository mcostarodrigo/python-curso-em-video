largura = float(input('\033[1:32mLargura da parede:\033[m '))
altura = float(input('\033[1:34mAltura da parede: \033[m'))
print(f'Sua parede tem a dimenção de {largura} x {altura} e sua área é de {largura * altura}m²')
print(f'Para pintar essa parede, você precisará de\033[1:32m {(largura * altura) / 2} \033[ml de tinta.')