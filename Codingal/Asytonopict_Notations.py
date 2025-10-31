def func1(n):
    iteration = 0 
    print("The number enter by the user is:", n)
    iteration += 1
    print("The number of iteration is:", iteration)
func1(5)

def func2(n):
    iteration = 0
    for i in range(1,n+1):
        iteration += 1
    print("The number of iteration is:", iteration,"The number enter by the user is:", n)
func2(5)

def func3(n):
    iteration = 0
    for i in range(0,n):
        for j in range(0,n):
            iteration += 1
    print("The number entered by the user is:", n,"The number of iteration is:", iteration)
func3(5)
