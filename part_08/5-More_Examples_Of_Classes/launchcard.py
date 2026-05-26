class LaunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def eat_launch(self):
        if self.balance >= 2.60:
            self.balance -= 2.60

    def eat_special(self):
        if self.balance >= 4.60:
            self.balance -= 4.60

    def deposit_money(self, amount: float):
        # negatif değerde para yuklenemez
        if amount < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")

        self.balance += amount

    def __str__(self):
        return f"The balance is {self.balance} euros"


# Test Alanı
if __name__ == "__main__":
    peters_card = LaunchCard(20)
    graces_card = LaunchCard(30)

    peters_card.eat_special()
    graces_card.eat_launch()

    print(f"Peter: {peters_card}")
    print(f"Grace: {graces_card}")

    peters_card.deposit_money(20)
    graces_card.eat_special()

    print(f"Peter: {peters_card}")
    print(f"Grace: {graces_card}")

    peters_card.eat_launch()
    peters_card.eat_launch()
    graces_card.deposit_money(50)

    print(f"Peter: {peters_card}")
    print(f"Grace: {graces_card}")

    # Çıkŧı:
    #
    # Peter: The balance is 15.4 euros
    # Grace: The balance is 27.4 euros
    # Peter: The balance is 35.4 euros
    # Grace: The balance is 22.799999999999997 euros
    # Peter: The balance is 30.199999999999996 euros
    # Grace: The balance is 72.8 euros

    # çıktıların hatalı görünmesinin sebebi float veri tipinin yapısından kaynaklanmaktadır
