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
f.close()


f1  = open("Tiger.txt", "r")
f2 = open("UpdatedTiger.txt", "w")
for i in f1.readlines():
    if not(i.startswith("The")):
        f2.write(i)

f1.close()
f2.close()

f = open("UpdatedTiger.txt", "r")
print(f.readlines())
f.close()