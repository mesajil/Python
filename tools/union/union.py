"""This App do the same as Google search bar"""


def read_data ():
    """Return a list: every line without its last line break"""
    path = r'input.txt'
    with open(path, 'r') as f:
        return [line.split('\n')[0] for line in f]


def write_data(data):
    """Write a string: Every line join by a CAR"""
    path = r'out.txt'
    with open(path, 'w') as f:
        CAR = ' '
        f.write(CAR.join(data))


def main():
    data = read_data()
    # print(data)
    write_data(data)


if __name__ == '__main__':
    main()