
#string con 5 palabras
s = 'leon tigre pantera jaguar guepardo'
#convirtiendo string a una lista
a = s.split()
#print de la lista
print (a)
#metodo uno
a.pop(3)
print(a)
#metodo dos
a.remove('leon')
#metodo tres
a.pop()
print(a)
#nueva lista ordenada (sort)
a.sort()
print(a)
#Agragando elementos a lista metodo uno
a.append("oso")
print(a)
#Agregando elementos a lista metodo dos
a.insert(0, "Jirafa")
print(a)
#agregando elementos a lista metodo 3
a.extend(["Hipopotamo"])
print(a)
#funcion Join
z = ', '.join(a)
print(z)

