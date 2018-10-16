f = open("text.txt", 'r')
words = 0
for line in f:
    wordslist = line.split()
    words = words + len(wordslist)
f.close()
print(words)