
def decorador (func):
    def interna(*args):
        print (f'Inicia la ajecucion de {func.__name__}')
        func(*args)
        print (f'Termina la ajecucion de {func.__name__}')
    return interna

@decorador
def hello (name):
    print (f'Hello {name}')

@decorador
def sumar (a, b):
    print (f'{a} + {b} = {a + b}')


# f = decorador(hello)
# f()

hello('Luis')
sumar(1,5)