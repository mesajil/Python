def esPar(num):
	par=0
	if num%2==0:
		par=1
	return par

# haga un programa que cuente cuántos números pares hay dentro un de array x

x = [11,14,15,13,12,21,24,25,20,31,43]

c=0
for i in range(len(x)):
	c = c+esPar(x[i])
	
print('En total hay ' + str(c) + ' números pares')