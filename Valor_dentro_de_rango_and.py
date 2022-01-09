a = int(input('Por favor ingresa un valor: '))
if a >= 0 and a <= 5:
    print(f'El numero {a} se encuentra dentro del rango')
else:
    print(f'El numero {a} no se encuentra dentro del rango')

#Otra manera de establecer el operador logico
rango = (a >= 0) and (a <=5)
if rango:
    print(f'El numero {a} se encuentra dentro del rango')
else:
    print(f'El numero {a} no se encuentra dentro del rango')
