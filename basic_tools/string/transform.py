



#Variables

OPTIONS_LIST = [str.capitalize, str.upper, str.lower]
LENGTH_MENU = 80


def print_menu ():
    print ("*"*LENGTH_MENU)
    print ("Hi all,")
    print ("transform your texts using the following functions:", end="\n\n")
    
    for i in range(len(OPTIONS_LIST)):
        print ((" [{}]. {} - {}").format(i+1, OPTIONS_LIST[i].__name__, OPTIONS_LIST[i].__doc__.replace("\n\n", " ").replace("\n", " ")))
    print ("*"*LENGTH_MENU, end="\n\n")

def get_str_list():
    print ("Enter texts to modify separated by commas:")
    return [s.strip() for s in input().split(",")]

def get_option_list ():
    print ("Enter the options numbers in order and separated by commas or spaces: ")
    return [int(s) for s in input ().replace(",", " ").split ()]

def transform_word (word, opt_list):
    for opt in opt_list:
        word = OPTIONS_LIST[opt-1](word)
    return word

def transform(str_list, opt_list):
    return [transform_word(s, opt_list) for s in str_list]

if __name__ == '__main__':
    
    print_menu()
    opt_list = get_option_list ()
    str_list = get_str_list ()
    print(transform(str_list, opt_list))