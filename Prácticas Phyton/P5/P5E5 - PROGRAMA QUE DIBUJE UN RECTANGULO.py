# JOSE MANUEL - P5E5 -  PROGRAMA QUE DIBUJE UN RECTÁNGULO

anchura = int(input('Anchura del rectángulo: '))
altura = int(input('Altura del rectángulo: '))

simbolo = '*'

for i in range(altura):
    print('', anchura * simbolo, '')
