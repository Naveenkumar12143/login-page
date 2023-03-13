#  Banking Application Deposit, withdraw, display

class Banking_appication():
    def __init__(self):
        self.amount = 0
    def deposit(self,Amount):
        self.amount += Amount
        print('Amount successfully Deposit')
    def withdraw(self,Amount):
        if (self.amount-Amount >=500):
            self.amount -= Amount
            print('Amount successfully withdraw')
        else:
            print('insufficient Bank /n you to keep at least Rs 500 in your account')
    def display(self):
        print("your Bank Balance is:", self.amount)

a = Banking_appication()
for i in range(0,50):
    print("1.Deposit, 2.withdraw, 3. Display, 4.exit")
    x = int(input("Enter your choice:"))
    if (x==1):
        Amount = float(input("Enter Amount to be deposit:"))
        a.deposit(Amount)
    elif (x==2):
        Amount = float(input("Enter Amount to be withdrawal:"))
        a.withdraw(Amount)
    elif (x==3):
        a.display()
    elif (x==4):
        exit()
    else:
        print("You Have Entered Wrong values")


