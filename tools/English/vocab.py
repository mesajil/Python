def get_data ():
    path = r'vocab.txt'
    with open(path, mode='r', encoding="utf8") as f:
        return [line for line in f]


def save_data(data):
    path = r'out.txt'
    with open(path, mode='w', encoding="utf8") as f:
        if isinstance(data, list):
            f.writelines(data)
        elif isinstance(data, str):
            f.write(data)


def main():
    data = get_data()
    data.sort(reverse=True)
    save_data(data)


if __name__ == '__main__':
    main()
