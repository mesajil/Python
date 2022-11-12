# 


def palindrome (text):
    return text == text[::-1]


def main():
    while True:
        text = input("Enter the value: ")
        print (palindrome(text))


if __name__ == "__main__":
    main()