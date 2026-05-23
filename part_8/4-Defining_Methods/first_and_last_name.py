class Person:
    def __init__(self, name: str):
        namesp = name.split(" ")
        self.firstName = namesp[0]
        self.lastName = namesp[-1]

    def return_first_name(self):
        return self.firstName

    def return_last_name(self):
        return self.lastName


if __name__ == "__main__":
    peter = Person("Peter Pythons")
    print(peter.return_first_name())
    print(peter.return_last_name())

    paula = Person("Paula Pythonnen")
    print(paula.return_first_name())
    print(paula.return_last_name())

    # Çıkŧı:
    #
    # Peter
    # Pythons
    # Paula
    # Pythonnen
