counts = dict()
line = input('Enter a line of text: ')
words = line.split()

print('Words:', 'a, b, c, d, e...')
print('Counting...')

for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)