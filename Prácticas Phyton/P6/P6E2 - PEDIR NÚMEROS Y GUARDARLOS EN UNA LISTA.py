# JOSE MANUEL - P6E2 - PEDIR NÚMEROS Y GUARDARLOS EN UNA LISTA.PARA TERMINAR DE INTRODUCIR
# UN NUMERO DECIR "SALIR"

numeros=[]
i=(input("Introduce una número: "))
salir=("salir")

while not i==salir:
    numeros.append(i)
    i=(input("Introduce un número mas: "))

print ("Los números que has escrito son",numeros,)
