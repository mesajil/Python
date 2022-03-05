


"""

Functions:


Get new line: Religiosas -> 1. Religiosas
sort list




"""




def get_lines (name):
    f = open (name, "r", encoding="utf8")
    lines = [line for line in f]
    f.close()
    return lines


def get_new_list(lines):
    index = 0
    sep = "."
    return [(line.split(sep))[index] + "\n" for line in lines] 

def print_list (l):
    [print(str(e)) for e in l]

def get_output_file (name, lines):
    f = open (name, "w")
    f.writelines(lines)
    f.close()

def get_sort_list(l):
    sorted = l[:]
    l.sort()
    return l

if __name__ == '__main__':
    inputname = "input.txt"
    outputname = "output.txt"
    index = 1
    functions = [get_new_list, get_sort_list]
    
    lines = get_lines (inputname)
    output = functions[index](lines)
    get_output_file (outputname, output)

    
