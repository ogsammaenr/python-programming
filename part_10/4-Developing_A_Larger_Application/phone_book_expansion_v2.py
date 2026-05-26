class Person:
    def __init__(self, name: str):
        self.__name = name
        self.__numbers = []
        self.__address = None

    def name(self) -> str:
        return self.__name

    def numbers(self) -> list:
        return self.__numbers

    def address(self) -> str | None:
        return self.__address

    def add_number(self, number: str):
        self.__numbers.append(number)

    def add_address(self, address: str):
        self.__address = address


class PhoneBook:
    def __init__(self):
        # str -> Person seklinde veri tutacak dictionary
        self.__persons = {}

    def add_number(self, name: str, number: str):
        # eger kisi ilk kez ekleniyorsa yeni bir person nesnesi olusturuyoruz
        if name not in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)

    def add_address(self, name: str, address: str):
        # eger kisi ilk kez ekleniyorsa yeni bir person nesnesi olusturuyoruz
        if name not in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(address)

    def get_entry(self, name: str) -> Person | None:  # Person veya None donebilir
        return self.__persons.get(name, None)


class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def search(self):
        name = input("name: ")
        person = self.__phonebook.get_entry(name)

        # kisi rehberde var mi
        if person is None:
            print("number unknown")
            print("address unknown")
            return

        # kisinin numarasi var mi
        if not person.numbers():
            print("number unknown")
        else:
            for number in person.numbers():
                print(number)

        # kisinin adresi var mi
        if person.address() is None:
            print("address unknown")
        else:
            print(person.address())

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()


# Test Alanı
if __name__ == "__main__":
    # ===============================================
    print("\n", "=" * 10, " Part 1 ", "=" * 10, "\n")

    person = Person("Eric")
    print(person.name())
    print(person.numbers())
    print(person.address())
    person.add_number("040-123456")
    person.add_address("Mannerheimintie 10 Helsinki")
    print(person.numbers())
    print(person.address())

    # ===============================================
    print("\n", "=" * 10, " Part 2 ", "=" * 10, "\n")

    phonebook = PhoneBook()
    phonebook.add_number("Eric", "02-123456")
    print(phonebook.get_entry("Eric"))
    print(phonebook.get_entry("Emily"))

    # ===============================================
    print("\n", "=" * 10, " Part 3 ", "=" * 10, "\n")

    application = PhoneBookApplication()
    application.execute()

    # Çıktı: (Girdiler = ['1', 'Eric', '02-123456', '3', 'Emily', 'Viherlaaksontie 7, Espoo', '2', 'Eric', '2', 'Emily', '3', 'Eric', 'Linnankatu 75, Turku', '2', 'Eric', '2', 'Wilhelm', '0'])
    #
    #  ==========  Part 1  ==========
    #
    # Eric
    # []
    # None
    # ['040-123456']
    # Mannerheimintie 10 Helsinki
    #
    # ==========  Part 2  ==========
    #
    # <__main__.Person object at 0x7f2844f78cd0>
    # None
    #
    # ==========  Part 3  ==========
    #
    # commands:
    # 0 exit
    # 1 add number
    # 2 search
    # 3 add address
    #
    # command: 1
    # name: Eric
    # number: 02-123456
    #
    # command: 3
    # name: Emily
    # address: Viherlaaksontie 7, Espoo
    #
    # command: 2
    # name: Eric
    # 02-123456
    # address unknown
    #
    # command: 2
    # name: Emily
    # number unknown
    # Viherlaaksontie 7, Espoo
    #
    # command: 3
    # name: Eric
    # address: Linnankatu 75, Turku
    #
    # command: 2
    # name: eric
    # number unknown
    # address unknown
    #
    # command: 2
    # name: wilhelm
    # number unknown
    # address unknown
    #
    # command: 0
