

"""
Examples

Generar a,b,c, ...
Generar A\nB\nC\n ...



"""
import string



def get_str ():
    str = string.ascii_lowercase
    sep = "\n"
    return sep.join(list(str))


if __name__ == '__main__':
    str = get_str()
    print (str)
