class BankAccount:
    def __init__(self, owner: str, account_number: str, balance: float):
        self.__owner = owner
        self.__account_number = account_number
        self.__balance = balance

    # getter metodu
    @property
    def balance(self) -> float:
        return self.__balance

    # işlem ücreti için private metod
    def __service_charge(self):
        self.__balance -= self.__balance * 0.01

    def deposit(self, amount: float):
        # negatif degerde para yuklenemez
        if amount < 0:
            return

        self.__balance += amount

        self.__service_charge()

    def withdraw(self, amount: float):
        # negatif degerde para yukleneemz
        if amount < 0:
            return

        self.__balance -= amount

        self.__service_charge()


if __name__ == "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)

    # Çıktı:
    #
    # 891.0
    # 981.09
