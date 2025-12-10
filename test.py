from trainingday1 import BankAccount
acc1 = BankAccount("Alice", 1000, "1234")
acc1.deposit(500)
acc1.withdraw(200, "1234")
print("Balance:", acc1.show_balance("1234"))
print("Transactions:", acc1.transaction_history)

acc2 = BankAccount.from_string("Bob,1500,5678")
acc2.deposit(300)
acc2.withdraw(100, "5678")
print("Balance:", acc2.show_balance("5678"))
print("Transactions:", acc2.transaction_history)

print(BankAccount.validate_amount(100))  
print(BankAccount.validate_amount(-50))  

print(hasattr(acc1, '__pin_code'))  
print(hasattr(acc1, '__transaction_history'))  
