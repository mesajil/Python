def factorial(n):
	f=1
	for i in range(1,n+1):
		f=f*i
	return f

def pedirInt(msj,li):
	while True:
		x = int(input(msj))
		if x>=li:
			break
	return x

a = pedirInt('Ingrese un número: ',0)
b = factorial(a)
print('El factorial de ' + str(a) + ' es ' + str(b))