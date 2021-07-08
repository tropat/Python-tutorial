file = open("file.txt","r") #"r","w","a"(append which means adding to a file),"r+"

print(file.readable())

print(file.readline()) #reads one line
print(file.readline()) #reads next line
#print(file.readlines()[1]) #reads all and put into a list
#print(file.read()) #reads all (in this example it reads all that remains)

for name in file.readlines():
    print(name)

file.close()

file = open("file.txt", "a")
file.write("Toby\n")
file.close()

file = open("file2.txt", "w")
file.write("Toby\n")
file.close()