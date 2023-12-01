import threading

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            print(f"Depositing {amount} dollars.")
            self.balance += amount
            print(f"New balance: {self.balance} dollars.")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                print(f"Withdrawing {amount} dollars.")
                self.balance -= amount
                print(f"New balance: {self.balance} dollars.")
            else:
                print("Insufficient funds!")

def perform_transactions(account, transactions):
    for transaction in transactions:
        action, amount = transaction
        if action == "deposit":
            account.deposit(amount)
        elif action == "withdraw":
            account.withdraw(amount)
        else:
            print(f"Unknown action: {action}")

if __name__ == "__main__":
    # Создайте банковский счет с начальным балансом в 1000 долларов
    account = BankAccount(balance=1000)

    # Определите список транзакций (формат: (действие, сумма))
    transactions = [
        ("deposit", 200),
        ("withdraw", 150),
        ("withdraw", 500),
        ("deposit", 100),
    ]

    # Создайте два потока для одновременного выполнения транзакций
    thread1 = threading.Thread(target=perform_transactions, args=(account, transactions))
    thread2 = threading.Thread(target=perform_transactions, args=(account, transactions))

    # Запустите потоки
    thread1.start()
    thread2.start()

    # Дождитесь завершения обоих потоков
    thread1.join()
    thread2.join()

    # Вывести окончательный баланс
    print(f"Final balance: {account.balance} dollars.")
