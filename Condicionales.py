
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