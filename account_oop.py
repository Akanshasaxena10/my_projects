class Account():
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance
        
        
    def deposit(self,dep_amt):
        self.balance = self.balance + dep_amt
        print(f'the add amount is {dep_amt} added to the balance.') 
        
    def withdrawal(self,w_amt):
        if self.balance >= w_amt:
            self.balance = self.balance - w_amt
            print(f'The withdraw amount {w_amt} is accepted and in process.')
        else:
            print('Insufficient balance')
            
    def __str__(self):
         return f'The owner of the account is {self.owner},The balance in your account is {self.balance}'  
a = Account('akki',400000)
b = Account('anuj',1000000)  
c = Account('ansh',1000) 
print(a.owner)    
print(b.owner)
print(a.balance) 
print(b.balance)
print(a)
print(b) 
a.deposit(2000)
print(a)
a.withdrawal(8000)
print(a) 
print(c) 
c.deposit(2000)  
print(c) 
c.withdrawal(2500)
print(c)
c.withdrawal(4500)
print(c)