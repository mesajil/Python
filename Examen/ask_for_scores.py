# escriba un programa que pide los datos academicos a un alumno: ciclo y 5 promedios (entero) de los cursos que lleva

def validarInt(msj,li,ls):
	while True:
		n = int(input(msj))
		if n>=li and n<=ls:
			break
	return n

ciclo = validarInt('Ingrese ciclo: ',1,10)
promedios = []
for i in range(1,6):
	p = validarInt('Ingrese promedio #' + str(i) + ': ',0,20)
	promedios.append(p)

print (promedios)