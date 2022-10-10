"""
Functions:

Modify text: a,b,c -> 1. a, 2. b, 3. c
get list of words: hello world -> hello, world
delete repeats: a b b c -> a b c

"""

def get_case_list (l, func):
    """
    a -> A
    """
    return [func(line) for line in l]

def get_words_list (lines):
    """
    Hello World ->  Hello
                    World
    """
    text = "".join(lines)
    return [word + "\n" for word in text.split()]



def get_modified_list(lines):
    """
    a, b, c -> a
    a -> a: 
    """
    #l = [(line.split(" "))[1] for line in lines] #
    l = [line.replace(" ","\t") for line in lines] # Change separator of 

    return l


def get_sort_list(l):
    aux = l[:]
    aux.sort()
    return aux

def print_list (l):
    [print(str(e)) for e in l]

def get_output_file (name, lines):
    f = open (name, "w", encoding="utf8")
    f.writelines(lines)
    f.close()

def get_lines (file):
    '''
    Return a list of lines from a file
    '''
    f = open (file, "r", encoding="utf8")
    lines = [line for line in f]
    f.close()
    return lines

def get_word_list_from_lyrics (lines):
    """
    A,B,C -> a,a,b,c ->     a   ->  a
                            a       b
                            b       c
                            c

    """
    output = get_case_list(lines, str.lower)
    output = get_words_list (output)
    output = list(set(output))
    return get_sort_list(output)

if __name__ == '__main__':
    INPUT_NAME = "song.txt"
    OUTPUT_NAME = "output.txt"
    
    lines = get_lines (INPUT_NAME)
    output = get_modified_list(lines)
    get_output_file (OUTPUT_NAME, output)

    
