#Виводить перші n рядків з фалу
def WriteLines(n):
    f = open("a.txt", 'r')
    for index, line in enumerate(f):
        if index >= n:
            break
        print (line)
    f.close()

#зчитує з файлу a
# та записує парні рядки у Верхньому регістрі в файл b1
# а непарні в нижньому регістрі в файл b2
def separ():
    f = open("a.txt", 'r')
    wparn = open('b1.txt', 'w')
    wneparn = open('b2.txt', 'w')
    for index, line in enumerate(f):
        if index % 2 == 0:
            print(index)
            print(line)
            wparn.write(line.upper())
        else:
            print(line)
            wneparn.write(line.lower())
    wparn.close()
    wneparn.close()
    f.close()


a = int(input("Enter number: "))
WriteLines(a)

separ()

