

def get_data ():
    path = r'subs.txt'
    with open(path, 'r') as f:
        text = ' '.join([line.replace('\n', '') for line in f if line != '\n'])
        return text


def save_data(data):
    path = r'out.txt'
    with open(path, 'w') as f:
        if isinstance(data, list):
            f.writelines(data)
        elif isinstance(data, str):
            f.write(data)


def main():
    data = get_data()
    # print(data)
    save_data(data)


if __name__ == '__main__':
    main()