# JOSE MANUEL - P5E7 -  PROGRAMA QUE DIBUJE UN TRIÁNGULO INVERTIDO

altura = int(input('Altura del triángulo: '))

simbolo = '*'

for i in range(altura):
    print('', simbolo * (altura - i), '')
