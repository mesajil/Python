


# haga un programa que solicite al usuario
# una oracion (x) y 2 palabras (a y b)
# el programa debe REEMPLAZAR todas las coincidencias
# de a en x, con b
# ej: 
# x = 'Udep Lima'
# a = 'Lima'
# b = 'Piura'
# resultado: x = 'Udep Piura'

while True:
	x = input('Ingrese una oración').strip()
	if x!='':
		break
while True:
	a = input('Ingrese la palabra a reemplazar').strip()
	if a!='':
		break
while True:
	b = input('Ingrese la palabra con la que se va a reemplazar').strip()
	if b!='':
		break


# con while p>-1
p = x.find(a)
while p>-1:
	y = x[0:p] 
	z = x[p+len(a):] 
	x = y+b+z
	p = x.find(a)

# con while True
while True:
	p = x.find(a)
	if p>-1:
		y = x[0:p] 
		z = x[p+len(a):] 
		x = y+b+z
	else:
		break

print(x)