def obtenerDigitos(num):
	d = []
	while num>0:
		d.append(num%10)
		num = int(num/10)
	return d

def sumaPotencias(arrNumeros,exponente):
	s=0
	for i in range(len(arrNumeros)):
		s = s + (arrNumeros[i]**exponente)
	return s


while True:
	x = int(input('Ingrese un número entero positivo: '))
	if x>0:
		break

digitos = obtenerDigitos(x)
#print(digitos)
numDigitos = len(digitos)
#print(numDigitos)
s = sumaPotencias(digitos,numDigitos)
#print(s)
if s==x:
	print('Sí cumple')
else:
	print('No cumple')