f=open("vaidu.txt","rt")        #Read-text mode is the default mode if we dont write r than it's ok
# f=open("vaidu.txt","rb")      #b & t are stand for binary and text mode if we want to openin binary or text
# a=f.read()                      #Heare we can also use the string split function
# for line in a:                #It will print the content character by character
#     print(line)

# for line in f:
#     print(line)
# print(f.readline())
print(f.readlines())            #This will store all line in the list and print
f.close()
