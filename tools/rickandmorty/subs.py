import re

def invalid_line(line):
    number = line.split('\n')[0].split(':')[0]
    return number.isnumeric() or number == ''


def get_data ():
    path = r'subs.txt'
    with open(path, 'r') as f:
        text = ' '.join([line.split('\n')[0].replace('<i>', '').replace('</i>', '') for line in f if not invalid_line(line)])
        skip = ['?', '-', '!', '.', ',']
        for c in skip: text = text.replace(c, c + '\n')
        return [line.strip(' -') + '\n' for line in text.split('\n') if len(line.strip(' -')) > 1]


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