f = open("Tiger.txt", "r")
print(f.readline())
f.close()

f = open("Tiger.txt", "r")
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

f = open("Tiger.txt", "r")
print(f.readlines())
f.close()

f = open("Tiger.txt", "r")
for i in f:
    print(i)
f.close()

f = open("Tiger.txt", "r")
print(f.read(20))