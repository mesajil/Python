# Simple Password Generator in Python


import string
import random


def generator2 (n1 = 0, n2 = 0, n3 = 0, n4 = 0):
    alphabet = []    
    alphabet += [random.choice(string.ascii_lowercase) for _ in range(n1)]
    alphabet += [random.choice(string.ascii_uppercase) for _ in range(n2)]
    alphabet += [random.choice(string.digits) for _ in range(n3)]
    alphabet += [random.choice(string.punctuation) for _ in range(n4)]
    random.shuffle (alphabet)
    return ''.join(alphabet)


def main():
    while True:
        x = int(input("Enter the value: "))
        print (generator2(x, x, x, x))
                

if __name__ == "__main__":
    main()