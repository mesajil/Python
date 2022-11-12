# Simple Password Generator in Python


import string
import random


def generator (length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join([random.choice(alphabet) for _ in range(length)])


def main():
    while True:
        length = int(input("Enter the value: "))
        print (generator(length))


if __name__ == "__main__":
    main()