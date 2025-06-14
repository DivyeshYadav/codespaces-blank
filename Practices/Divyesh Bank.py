class bank:
    def __init__(self,name,):
        self.name = name
        self.balance = 0.00
    def check_balance(self):
        print(f"Your balance in {self.name} is {self.balance}")
    def deposit(self,amount):
        self.balance=self.balance+amount 
        print(f"Rs.{amount} has been sucessfully deposited in {self.name} ")
    def witdraw(self,amount):
        self.balance=self.balance-amount
db = bank("Divyesh Bank")       
while(True):
        print(f"Wlecome to {db.name}.Please choose any one option below(1-3)")
        print("1.Check Balance")
        print("2.Deposit")
        print("3.Withdraw")
        choice = int(input(""))
        if choice == 1:
            db.check_balance()
        elif choice == 2:
            amount=float(input("Please enter how much Rs you want to deposit: "))
            db.deposit(amount)
        elif choice == 3:
            amount=float(input("Please enter how much Rs you want to withdraw: "))
            db.witdraw(amount)   