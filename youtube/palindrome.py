

def palindrome (text):
    return text == text[::-1]


def main():
    text = input('Text: ')
    if palindrome(text): print(f'{text} is polindrome')
    else: print(f'{text} is not polindrome')


if __name__ == "__main__":
    main()