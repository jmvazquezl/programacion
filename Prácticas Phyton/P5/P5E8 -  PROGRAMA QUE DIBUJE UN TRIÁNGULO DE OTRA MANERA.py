# JOSE MANUEL - P5E8 -  PROGRAMA QUE DIBUJE UN TRIÁNGULO DE OTRA MANERA

altura = int(input('Altura del triángulo: '))

simbolo = '*'

for i in range(altura):
    print('', (i + 1) * simbolo, '')

for j in range(altura + 1):
    print('', simbolo * (altura - (j - 1)), '')


