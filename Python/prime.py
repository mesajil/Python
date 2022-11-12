#


def prime (number):
    return not any( [number % x == 0 for x in range(2,number)] )


def main():
    while True:
        number = int(input("Enter the value: "))
        print (prime(number))


if __name__ == "__main__":
    main()