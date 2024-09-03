'''
write a python program to create account class and create credit and debit methods.
'''
class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def credit(self, amount):
        self.balance += amount
        print(amount, 'added to your account and the balance is ', self.balance)

    def debit(self, amount):
        self.balance -= amount
        print(amount, 'debited from your account and the balance is ', self.balance)



acc1 = Account(10000, 12345)
acc1.credit(4000)
acc1.debit(2500)

'''Write a Python program to create a person class. Include attributes  
like name, country and date of birth. Implement a method to  determine the person’s age.''' 

from datetime import date
class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob
    
    def get_age(self):
        today_date = date.today()
        age = today_date.year - self.dob.year

        if ((today_date.month, today_date.day)< (self.dob.month, self.dob.day)):
            age -=1
        return age

        

p1 = Person('nikita', 'india', date(2001,7,25))
print(p1.get_age())