with open("Sample.txt","w") as f:
    f.write("Hello my name is Divyesh. I am 10 years old. I am lering Python. I love to code.")
f.close()

file = open("Sample1.txt", "x")
file.close()

f= open("Sample.txt", "r")
word = f.readlines()
for i in word:
    line= i.split()
    print(line)
f.close()
import os
if os.path.exists("Sample.txt"):
    print("This File exists")
else:
    print("This File does not exists")

os.remove("Sample1.txt")
#os.rmdir("example")
    
