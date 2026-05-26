class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self) -> str:
        return self.__name

    # getter
    def weight(self) -> int:
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.items = []

    # getter
    def weight(self) -> int:
        return sum(item.weight() for item in self.items)

    def add_item(self, item: Item):
        # limitin asilmadigini kontrol edip ekliyoruz
        if self.weight() + item.weight() <= self.max_weight:
            self.items.append(item)

    def print_items(self):
        for item in self.items:
            print(item)

    def heaviest_item(self) -> Item | None:  # Item veya None döndürebilir
        # eger hic ekleme islemi yapilmadiysa None donduruyoruz
        if not self.items:
            return None
        # itemlerin agirliklarina gore en buyugu buluyoruz
        return max(self.items, key=lambda item: item.weight())

    def __str__(self):
        count = len(self.items)
        # dil bilgisi kontrolu
        item_string = "item" if count == 1 else "items"
        return f"{count} {item_string} ({self.weight()} kg)"


class CargoHold:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.suitcases = []

    # toplam agirligi suitcases listesindeki elemanlarin agirliklarini toplayarak hesapliyoruz
    def total_weight(self) -> int:
        return sum(suitcase.weight() for suitcase in self.suitcases)

    def add_suitcase(self, suitcase: Suitcase):
        # limitin asilmadigini kontrol edip listeye ekliyoruz
        if self.total_weight() + suitcase.weight() <= self.max_weight:
            self.suitcases.append(suitcase)

    def print_items(self):
        for suitcase in self.suitcases:
            suitcase.print_items()

    def __str__(self):
        count = len(self.suitcases)
        # dil bilgisi kontrolu
        sutcase_str = "suitcase" if count == 1 else "suitcases"

        # kalan bos alani hesapliyoruz
        space_left = self.max_weight - self.total_weight()
        return f"{count} {sutcase_str}, space for {space_left} kg"


if __name__ == "__main__":
    # part 1
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)

    print("Name of the book:", book.name())
    print("Weight of the book:", book.weight())

    print("Book:", book)
    print("Phone:", phone)

    # =========================================
    print("\n", "=" * 50, "\n")

    # part 2
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(5)
    print(suitcase)

    suitcase.add_item(book)
    print(suitcase)

    suitcase.add_item(phone)
    print(suitcase)

    suitcase.add_item(brick)
    print(suitcase)

    # =========================================
    print("\n", "=" * 50, "\n")

    # part 4
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(10)
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)

    print("The suitcase contains the following items:")
    suitcase.print_items()
    combined_weight = suitcase.weight()
    print(f"Combined weight: {combined_weight} kg")

    # =========================================
    print("\n", "=" * 50, "\n")

    # part 5
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(10)
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)

    heaviest = suitcase.heaviest_item()
    print(f"The heaviest item: {heaviest}")

    # =========================================
    print("\n", "=" * 50, "\n")

    # part 6
    cargo_hold = CargoHold(1000)
    print(cargo_hold)

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold.add_suitcase(adas_suitcase)
    print(cargo_hold)

    cargo_hold.add_suitcase(peters_suitcase)
    print(cargo_hold)

    # =========================================
    print("\n", "=" * 50, "\n")

    # part 7
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()

    # Çıktı:
    #
    # Name of the book: ABC Book
    # Weight of the book: 2
    # Book: ABC Book (2 kg)
    # Phone: Nokia 3210 (1 kg)
    #
    # ==================================================
    #
    # 0 items (0 kg)
    # 1 item (2 kg)
    # 2 items (3 kg)
    # 2 items (3 kg)
    #
    # ==================================================
    #
    # The suitcase contains the following items:
    # ABC Book (2 kg)
    # Nokia 3210 (1 kg)
    # Brick (4 kg)
    # Combined weight: 7 kg
    #
    # ==================================================
    #
    # The heaviest item: Brick (4 kg)
    #
    # ==================================================
    #
    # 0 suitcases, space for 1000 kg
    # 1 suitcase, space for 997 kg
    # 2 suitcases, space for 993 kg
    #
    # ==================================================
    #
    # The suitcases in the cargo hold contain the following items:
    # ABC Book (2 kg)
    # Nokia 3210 (1 kg)
    # Brick (4 kg)
