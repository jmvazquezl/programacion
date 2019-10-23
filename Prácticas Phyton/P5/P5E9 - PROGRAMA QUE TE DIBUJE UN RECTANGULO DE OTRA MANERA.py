# JOSE MANUEL - P5E9 -  PROGRAMA QUE DIBUJE UN RECTANGULO DE OTRA MANERA

anchura = int(input('Anchura del rectángulo: '))
altura = int(input('Altura del rectángulo: '))

print(anchura * '*')

for i in range(altura - 2):
    print('*',(' ' * (anchura - 4)),'*',)

print(anchura * '*')
