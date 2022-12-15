print(20 * '-=')
print('Analisador de Triângulos')
print(20 * '-=')
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 + s2 > s3 and s2 + s3 > s1 and s2 + s3 > s1:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima NÃO podem formar um triângulo!')
