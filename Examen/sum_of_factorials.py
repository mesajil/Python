# escriba una funcion que reciba como parámetros 
#  un límite inferior y un límite superior
# y retorne la suma de los factoriales entre dichos límites
# ej: li:a, ls:b -: factorial(a)+factorial(a+1)+....factorial(b)

def factorial(n):
	f=1
	for i in range(1,n+1):
		f=f*i
	return f

def sumaFactoriales(li,ls):
	s=0
	for i in range(li,ls+1):
		s = s + factorial(i)
	return s

print(sumaFactoriales(1,5))
