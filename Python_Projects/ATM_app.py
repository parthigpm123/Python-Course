class ATM:
      def __init__(self,balance=1000):
            self.balance=balance
       # Check balance method     
      def check_balance(self):
            return f" Your Account Balance is:{self.balance} "
      #Deposit Method
      def deposit(self,amount):
            self.balance+=amount
            return f" Deposited ${amount}. Your new Balance is: ${self.balance}"
      #Withdraw method 
      def withdraw(self,amount):
            if self.balance >= amount:
                  self.balance-=amount
                  return f"withdrew ${amount}. Your new balance is: ${self.balance}"
            else:
                  return "insufficient funds. Withdrawal failed."
       #Exit method     
      def exit(self):
            return input("Give Your Feedback : Good🧡🧡🧡 Average🧡🧡 Bad🧡:")     
                  
atm=ATM()

while True:
      print("\nWELCOME TO INDIAN BANK ATM SERVICES")
      print("1. Check Balance")
      print("2. Deposit")
      print("3. Withdraw")
      print("4. Exit")
      
      choice=input("Enter Your Choice:")
      
      if choice=="1":
            print(atm.check_balance())
      elif choice =="2":
            amount=float(input("Enter The Deposit Amount:"))
            print(atm.deposit(amount))
            
      elif choice =="3":
            amount = float(input('Enter the withdrawal amount'))
            print(atm.withdraw(amount)) 
      elif choice =="4":
            print(atm.exit())
            print("Thank You For visiting Our Indian Atm Service")   
    
            break        
      
                        
            
            