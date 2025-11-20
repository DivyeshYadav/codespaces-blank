number = int(input("Enter a number to check: "))
o_num = number
rev_num = 0
while number > 0:
    digit = number % 10
    rev_num = rev_num * 10 + digit
    number = number // 10

if o_num == rev_num:
    print("This number is a palindrome")
else:
    print("This number is not a palindrome")

