
def invalid_line(line):
    """Return True if line is numeric or empty"""
    number = line.split('\n')[0].split(':')[0]
    return number.isnumeric() or number == ''


def get_lines ():
    """Return a list: text splited by line breakers"""
    skip = ['?', '-', '!', '.', ',']
    for c in skip:
        text = text.replace(c, c + '\n')
    return text.split('\n')


def read_data ():
    path = r'subs.txt'
    with open(path, 'r') as f:
        # Text: All of no numeric lines without <i> and </i>
        text = ' '.join([line.split('\n')[0].replace('<i>', '').replace('</i>', '') for line in f if not invalid_line(line)])
        
        # Return every line separated by line breakers with length greater than one
        return [line.strip(' -') + '\n' for line in get_lines(text) if len(line.strip(' -')) > 1]


def write_data(data):
    path = r'out.txt'
    with open(path, 'w') as f:
        if isinstance(data, list):
            f.writelines(data)
        elif isinstance(data, str):
            f.write(data)


def main():
    data = read_data()
    # print(data)
    write_data(data)


if __name__ == '__main__':
    main()