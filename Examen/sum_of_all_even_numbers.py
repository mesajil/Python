def esPar(num):
	par=0
	if num%2==0:
		par=1
	return par

# haga un programa que sume
# todos los valores pares de un array

x = [11,14,15,13,12,21,24,25,20,31,43,30]

s=0
for i in range(len(x)):
	s = s + x[i]*esPar(x[i])
	# if esPar(x[i])==1:
	# 	s = s + x[i]

print('La suma de los pares es ' + str(s))