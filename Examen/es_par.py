def esPar(num):
	par=0
	if num%2==0:
		par=1
	return par

# haga un programa que imprima los 10 primeros números pares positivos
i=1
c=0
while c<10:
	if esPar(i)==1:
		print(i)
		c=c+1
	i=i+1