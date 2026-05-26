class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value

    def print_value(self):
        print("value:", self.value)

    # degeri 1 azaltiyoruz
    def decrease(self):
        self.value -= 1


# Test Alanı
if __name__ == "__main__":
    counter = DecreasingCounter(10)
    counter.print_value()

    counter.decrease()
    counter.print_value()

    counter.print_value()
    counter.decrease()

    # Çıktı:
    #
    # value: 10
    # value: 9
    # value: 9
