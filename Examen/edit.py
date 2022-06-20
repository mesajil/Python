def diasAño(a):
	return 365 + esBisiesto(a)

def esBisiesto(a):
	if a%4==0 and (a%100!=0 or a%400==0):
		return 1
	else:
		return 0

def numDias(m,a):
	dias = [31,28,31,30,31,30,31,31,30,31,30,31]
	dias[1] = dias[1]+esBisiesto(a)
	return dias[m-1]

def diasDesde(d,m,a):
	# Días desde que empezó el año hasta la fecha dada
	s=0
	for i in range(1,m):
		s = s + numDias(i,a)
	s = s + d
	return s

def diasAcabe(d,m,a):
	return diasAño(a) - diasDesde(d,m,a)

def pedirNumero(msj,minimo,maximo):
	while True:
		numero = int(input(msj))
		if numero>=minimo and numero<=maximo:
			break
	return numero

a1 = pedirNumero('Ingrese año de la fecha 1: ',1900,2099)
m1 = pedirNumero('Ingrese mes de la fecha 1: ',1,12)
d1 = pedirNumero('Ingrese día de la fecha 1: ',1,numDias(m1,a1))

a2 = pedirNumero('Ingrese año de la fecha 2: ',a1,2099)

if a2>a1:
	minM=1
else:
	minM=m1
m2 = pedirNumero('Ingrese mes de la fecha 2: ',minM,12)

if a2>a1 or (a2==a1 and m2>m1):
	minD = 1
else:
	minD = d1+1
d2 = pedirNumero('Ingrese día de la fecha 2: ',minD,numDias(m2,a2))

# cuántos días han pasado desde que empezó el año para la fecha 1?
c1 = diasDesde(d1,m1,a1)-1
print('Han pasado ' + str(c1) + ' días')

# cuántos días faltan para que acabe el año de la fecha 2?
c2 = diasAcabe(d2,m2,a2)
print('Faltan ' + str(c2) + 'dias')

# cuántos días han transcurrido entre fecha 1 y fecha 2

if a1==a2:
	c1 = diasDesde(d1,m1,a1)
	c2 = diasDesde(d2,m2,a2)
	print('Han transcurrido ' + str(c2-c1) + ' días')

else:

	c1 = diasAcabe(d1,m1,a1)
	c2 = diasDesde(d2,m2,a2)

	c3 = 0
	for i in range(a1+1,a2):
		c3 = c3 + diasAño(i)

	print('Han transcurrido ' + str(c1+c2+c3) + ' días')