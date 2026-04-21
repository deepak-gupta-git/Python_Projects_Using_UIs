file = open("shyam.txt" , "w")
file.write("hello from file handling this is most important topic in python.")


file = open("shyam.txt", "r")
content = file.read()
print(content)
file.close()

