#necesito crear un programa que almacene una lista de 200 notas
import random

notas=[]
for i in range (5):

    notaSimulada=random.randint(1,5)
    notas.append(notaSimulada)



#Metodos para transformar, modificar o administrar listas
notas.insert(0,80)
notas.remove(80)
notas.pop(0)
notas.sort(reverse=True)
#notas.clear()
print(notas)