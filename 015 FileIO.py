f=open("vaidu.txt","rt")        #Read-text mode is the default mode if we dont write r than it's ok
# f=open("vaidu.txt","rb")      #b & t are stand for binary and text mode if we want to openin binary or text
# a=f.read()                      #Heare we can also use the string split function
# for line in a:                #It will print the content character by character
#     print(line)

# for line in f:
#     print(line)
# print(f.readline())
#print(f.readlines())            #This will store all line in the list and print
#f.close()

# f = open("vaiduu.txt", "w")
# a = f.write("Viadu will became great hacker of the history\n")
# print(a)
# f.close()

# f = open("vaiduu.txt", "a")
# a = f.write("Viadu will became great hacker of the history\n")
# print(a)
# f.close()

# f = open("vaiduu.txt", "w")
# a = f.write("Viadu will became great hacker of the history\n")
# print(a)
# f.close()

# handle read and write both
# f = open("vaiduu.txt", "r+")
# print(f.read())
# f.write("As soon as")

f=open("vaiduu.txt")
# print(f.tell())             # tell() function give information about character position of file function 'f'
print(f.readline())
f.seek(10)                     # seek() function will reset the position of file function f to the given position in argument
# print(f.tell())
print(f.readline())
# print(f.tell())

