# lista
# indice  0        1         2          3        4
lista=["lunes","martes","miercoles","jueves","viernes"]
print(lista)
print(lista[2]) # desde el indice 0 al 2 --no imprime el ultimo
print(lista[-2]) #empieza desde el ultimo elemento
print(lista[0:3])
print(lista[2:]) # desde el indice 2 al final
print(lista[-3:])#desde el ultimo indice hasta el -3
    
lista[2]= "sabado" #remplazar un elemento de la lista
print(lista)
for listas in lista: # imprime uno por uno
    print(listas)

def listilla(lista):
    if "sabado" in lista:
        return 1
if listilla == 1:
    print("hola")