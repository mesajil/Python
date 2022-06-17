

"""

Inputs:


Examples outputs

a,b,c, ...
A\nB\nC\n ...



"""
import string



def get_str ():
    str = string.ascii_uppercase
    sep = "\n"
    return sep.join(list(str))


if __name__ == '__main__':
    str = get_str()
    print (str)
