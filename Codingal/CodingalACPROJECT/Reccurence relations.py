def myfunction1(n):
    if n <= 0:
        return
    for i in range(0, n + 1):
        print("Codingal")
    myfunction1(n // 2)
    myfunction1(n // 3)


def myfunction2(n):
    if n <= 1:
        return
    print("Codingal")
    myfunction2(n - 1)



def print_analysis():
    print("myfunction1(n)")
    print(" The function prints 'Codingal' n times.")
    print(" Then it calls itself with n/2 and n/3.")
    print(" So it keeps getting smaller and smaller.")
    print(" Total Time = O(n)")
    print("   (This means: the work grows almost the same as n.)\n")

    print("myfunction2(n)")
    print(" The function prints 'Codingal' once each time.")
    print(" Then it calls itself again with n-1.")
    print(" It keeps going until it reaches 1.")
    print(" Total Time = O(n)")
    print("   (This means: it repeats the work n times.)\n")


print_analysis()

