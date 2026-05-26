# --- KATMAN 1: UYGULAMA MANTIĞI (APPLICATION LOGIC) ---
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if name not in self.__persons:
            self.__persons[name] = []
        self.__persons[name].append(number)

    def get_numbers(self, name: str):
        if name not in self.__persons:
            return None
        return self.__persons[name]

    def all_entries(self):
        return self.__persons

    def get_name(self, number: str):
        # teker teker numarayi ariyoruz
        for name, numbers in self.__persons.items():
            if number in numbers:
                return name
        return None


class FileHandler:
    def __init__(self, filename: str):
        self.__filename = filename

    def load_file(self):
        names = {}
        try:
            with open(self.__filename) as f:
                # ';' sembolunden ayirarak isim ve numara listesini olusturuyoruz
                for line in f:
                    parts = line.strip().split(";")
                    name, *numbers = (
                        parts  # ilk eleman isim sonraki elemnalar isim listesini olusturuyor
                    )
                    names[name] = numbers
        except FileNotFoundError:
            # hata durumunda uygulamayi bozmuyoruz
            pass
        return names

    def save_file(self, phonebook: dict):
        with open(self.__filename, "w") as f:
            for name, numbers in phonebook.items():
                line = [name] + numbers
                # veriler arasina ';' sembolu ekleyerek dosyaya yazdiriyoruz
                f.write(";".join(line) + "\n")


class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
        self.__filehandler = FileHandler("phonebook.txt")

        for name, numbers in self.__filehandler.load_file().items():
            for number in numbers:
                self.__phonebook.add_number(name, number)

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add entry")
        print("2 search")
        print("3 search by number")

    def add_entry(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_numbers(name)
        if numbers is None:
            print("number unknown")
            return
        for number in numbers:
            print(number)

    def search_by_number(self):
        number = input("number: ")
        name = self.__phonebook.get_name(number)

        if name is not None:
            print(name)
        else:
            print("unknown number")

    def exit(self):
        # uygulama kapanirken dosyaya kayit aliyoruz
        self.__filehandler.save_file(self.__phonebook.all_entries())

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                self.exit()
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            elif command == "3":
                self.search_by_number()
            else:
                self.help()


# Test Alanı
if __name__ == "__main__":
    application = PhoneBookApplication()
    application.execute()

    # Çıktı: (Girdiler = ['1', 'Eric', '02-123456', '1', 'Eric', '045-4356713', '3', '02-123456', '3', '0100100', '0'])
    #
    # commands:
    # 0 exit
    # 1 add entry
    # 2 search
    # 3 search by number
    #
    # command: 1
    # name: Eric
    # number: 02-123456
    #
    # command: 1
    # name: Eric
    # number: 045-4356713
    #
    # command: 3
    # number: 02-123456
    # Eric
    #
    # command: 3
    # number: 0100100
    # unknown number
    #
    # command: 0
