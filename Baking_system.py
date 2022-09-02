class User():
    def __init__(self, Name, Age, Gender):
        self.Name=Name
        self.Age=Age
        self.Gender=Gender
    def ShowDetails(self):
        print("Important Details are..")
        print("")
        print("Name is : ",self.Name)
        print("Age is : ",self.Age)
        print("Gender is : ",self.Gender)

class Bank(User):
    def __init__(self, Name, Age, Gender):
        super().__init__(Name,Age,Gender)
        self.Balance=0

    def Deposite(self, Amount):
        self.Amount=Amount
        self.Balance=self.Balance+self.Amount
        print("your Balance is   :",self.Balance,"$")

    def Withdraw(self,Amount):
        self.Amount=Amount
        if (self.Amount>self.Balance):
            print("insufficient account Balance..",self.Balance)
        else:
            self.Balance=self.Balance-self.Amount
            print("Account balance is updated by..",self.Balance)

    def View_Balance(self):
        self.ShowDetails()
        print("Available Balance is : ",self.Balance)


Mari = Bank("Mari",21,"Male")
Mari.Deposite(5000)
Mari.Deposite(5000)
Mari.Withdraw(2000)
Mari.Withdraw(2000)
Mari.ShowDetails()
Mari.View_Balance()
# Mari.Withdraw(20000)
# Mari.ShowDetails()
print(Mari.Name)
print(Mari.Gender)
print(Mari.Age)