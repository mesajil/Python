


if __name__ == '__main__':

    INPUT_FILE = "song.txt"
    OUTPUT_FILE = "words.txt"

    f = open (INPUT_FILE, "r", encoding="utf8")
    
    # Get set of words from the file
    words = set()
    for line in f:
        l = line.split()
        l = [e.lower() + "\n" for e in l] # Low each word and add an \n 
        words.update(l)
    f.close()

    l = list(words)  
    l.sort()

    f = open (OUTPUT_FILE, "w", encoding="utf8")
    f.writelines(l)
    f.close()

