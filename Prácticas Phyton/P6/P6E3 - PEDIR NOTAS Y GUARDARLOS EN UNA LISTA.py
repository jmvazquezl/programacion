# JOSE MANUEL - P6E3 - PEDIR NOTAS Y GUARDARLOS EN UNA LISTA.PARA TERMINAR DE INTRODUCIR
# UN NOTA QUE NO ESTÉ ENTRE 0 Y 10

notas=[]
i=float(input("Introduce una nota: "))

while i>=0 and i<=10:
    notas.append(i)
    i=float(input("Introduce un número mas: "))

print ("Los notas que has escrito son",notas,)
