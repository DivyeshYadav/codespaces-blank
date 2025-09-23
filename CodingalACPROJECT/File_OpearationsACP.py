f = open("Lion.txt", "r")
print(f.readline())
f.close()

f = open("Lion.txt", "r")
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

f = open("Lion.txt", "r")
print(f.readlines())
f.close()

f = open("Lion.txt", "r")
for i in f:
    print(i)
f.close()

f = open("Lion.txt", "r")
print(f.read(20))
f.close()


f1  = open("Lion.txt", "r")
f2 = open("UpdatedLion.txt", "w")
for i in f1.readlines():
    if not(i.startswith("The")):
        f2.write(i)

f1.close()
f2.close()

f = open("UpdatedLion.txt", "r")
print(f.readlines())
f.close()