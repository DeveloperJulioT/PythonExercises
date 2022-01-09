diccionario = {
    'nombres' :['Daniel','Andres','Javier','Lucia','Kelly'], 
    'edad' : [22, 25, 45, 53, 12], 
    'mes': ['Enero','marzo','Diciembre','Octubre','Enero'],
    'dia': [25, 12, 29, 19, 31]
}
print (diccionario)
print('')

#print (diccionario['nombres'])
#print (diccionario['edad'])
#print (diccionario['mes'])
#print (diccionario['dia'])

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        for item in val:
            if item not in inverse:
                inverse[item]=[key]
            else:
                inverse[item].append(key)
    return inverse  

inverted_diccionario = invert_dict(diccionario)
print (inverted_diccionario)
    

