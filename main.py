
def max(a, b):
    if a < b:
        print(b)
    elif a > b:
        print(a)
    else:
        print ("Los numeros son iguales")
max(1,0)


def max(a, b, c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    elif c > a and c > b:
        print (c)
    else:
        print ("Los numeros son iguales")
max(3, 3, 3)

print("Por favor ingrese su edad")
edad = int(input())

if edad > 18:
    print("Mayor de Edad")
else:
    print("Menor de edad")


#############################################################################################################################################################
x = 10
y = 2
z = x + y
#Posicion de memoria donde se encuentra el valor que almacena la variable en este caso (x). (Direccion de memoria)
print(id(x))
print(id(y))
print(id(z))

x = 10
#Tipo de la viriable (Tipo de dato)
print(type(x))
x = "Hola Mundo"
print(type(x))
x = False
print(type(x))

#Concatenacion
MiGrupoFavorito = "Aerosmith"
Comentario = "The best rock band"
#Formas de imprimir concatenando con (+) o usando (,)
print ("Mi Grupo Favorito es: " + MiGrupoFavorito + " " + Comentario)
print("Mi Grupo favorito es:", MiGrupoFavorito, Comentario)

#Convertir cadena a entero
numero1 = "1"
numero2 = "2"
print("Concatenacion:", numero1 + numero2)
print("suma:", int(numero1) + int (numero2)) 

#tipos bool (Boolean)
miVariable = False
print(miVariable)
#La variable toma valor de False o True
miVariable = 1 > 2
print(miVariable)
#Si es True
if miVariable:
    print("El resultado fue verdadero")
#si es False
else:
    print("Elresultado fue falso")

#Funcion input para procesar la entrada del usuario
resultado = input()
print(resultado)

numero1 = input("Ingrese el primer numero: ")
numero2 = input("Ingrese el segundo numero: ")
suma = numero1 + numero2
print ("la suma de los numeros es: ", suma)