from datetime import datetime

class BankAccount:
    def __init__(self, account_holder, balance, pin_code):
        self.account_holder = account_holder
        
        if not self.validate_amount(balance):
            raise ValueError("Balance must be a non-negative number.")
        self._balance = balance
        
        self.__transaction_history = []
        if not self.validate_pin(pin_code):
            raise ValueError("PIN must be a 4-digit numeric string.")
        self.__pin_code = pin_code
    @property
    def balance(self):
        return self._balance

    @property
    def transaction_history(self):
        return self.__transaction_history.copy()

    def record_transaction(self, permitted, action, amount=0):
        self.__transaction_history.append({
            "permitted": permitted,
            "action": action,
            "amount": amount,
            "date": datetime.now()
        })

    def deposit(self, amount):
        if not self.validate_amount(amount):
            raise ValueError("Amount must be a non-negative number.")
        self._balance += amount
        self.record_transaction(True, "deposit", amount)

    def withdraw(self, amount, pin):
        if pin != self.__pin_code:
            self.record_transaction(False, "withdraw", amount)
            raise PermissionError("Incorrect PIN.")
        if not self.validate_amount(amount):
            raise ValueError("Amount must be a non-negative number.")
        if amount > self._balance:
            self.record_transaction(False, "withdraw", amount)
            raise ValueError("Insufficient balance.")
        self._balance -= amount
        self.record_transaction(True, "withdraw", amount)

    def show_balance(self, pin):
        if pin != self.__pin_code:
            self.record_transaction(False, "show_balance")
            raise PermissionError("Incorrect PIN.")
        self.record_transaction(True, "show_balance")
        return self._balance

    @classmethod
    def from_string(cls, data_str):
        parts = data_str.split(",")
        if len(parts) != 3:
            raise ValueError("String must be in format 'name,balance,pin'")
        name = parts[0]
        balance = float(parts[1])
        pin = parts[2]
        return cls(name, balance, pin)

    @staticmethod
    def validate_amount(amount):
        return isinstance(amount, (int, float)) and amount >= 0
    
    @staticmethod
    def validate_pin(pin):
        return isinstance(pin, str) and pin.isdigit() and len(pin) == 4