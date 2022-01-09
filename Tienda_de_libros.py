print('Proporcione los siguientes datos del libro \n')
nombre = input('Ingrese el nombre del libro: ')
id = int(input('Ingrese el Id del libro: '))
precio = float(input('Ingrese el precio del libro: '))
envio = (input('Indicar si el envio es gratuito (True/False): '))
if envio == 'True':
    envio = True
elif envio == 'False':
    envio = False
else:
    envio = 'Valor incorrecto, debe escribir (True / False)'

print(f'Nombre: {nombre} \nId: {id} \nPrecio: {precio} \nEnvio gratuitio ?: {envio}')