# escriba un programa que solicite al usuario un texto
# y lo convierta en un array de palabras

while True:
	x = input('Ingrese un texto').strip()
	if x!='':
		break

print(x)

arreglo = []
p = x.find(' ')
while p>-1:
	palabra = x[0:p]
	arreglo.append(palabra)

	x = x[p+1:] # elimino la 1ra palabra y el 1er espacio
	#x = x[p:].strip()
	p = x.find(' ')
	print(x)
	print(arreglo)

arreglo.append(x)
print(arreglo)
print(len(arreglo))

# validar cantidad de palabras: exacta, minima, maxima del texto
# validar la presencia o ausencia de una palabra en el texto
