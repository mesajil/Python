

path = r'subs.txt'
with open(path, 'r') as f:
    text = ' '.join([line.replace('\n', '') for line in f if line != '\n'])
print (text)
with open('text.txt', 'w') as f:
    f.write(text)