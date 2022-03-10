"""
Functions:

Modify text: a,b,c -> 1. a, 2. b, 3. c
sort list: a,c,b -> a,b,c
get list of words: hello world -> hello, world
delete repeats: a b b c -> a b c
get_case_list: a b c -> A B C



"""

def get_case_list (l, func):
    return [func(line) for line in l]


def get_lines (name):
    f = open (name, "r", encoding="utf8")
    lines = [line for line in f]
    f.close()
    return lines


def get_sub_list(lines):
    index = 0
    sep = "."
    return [(line.split(sep))[index] + "\n" for line in lines] 

def print_list (l):
    [print(str(e)) for e in l]

def get_output_file (name, lines):
    f = open (name, "w", encoding="utf8")
    f.writelines(lines)
    f.close()

def get_sort_list(l):
    aux = l[:]
    aux.sort()
    return aux

if __name__ == '__main__':
    inputname = "input.txt"
    outputname = "output.txt"
    
    lines = get_lines (inputname)
    #print_list(lines)
    output = get_case_list(lines, str.lower)
    output = get_sort_list(output)
    get_output_file (outputname, output)

    
