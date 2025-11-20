largest_number = int(input("Enter the largest number: "))
smallest_number = int(input("Enter the smallest number: "))

while(smallest_number):
    numberstore = smallest_number
    smallest_number = largest_number % smallest_number
    largest_number = numberstore
print("The HCF is:", largest_number)