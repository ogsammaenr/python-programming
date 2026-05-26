class Present:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight} kg)"


class Box:
    def __init__(self):
        self.presents = []

    def add_present(self, present: Present):
        self.presents.append(present)

    def total_weight(self):
        # presents listesindeki nesnelerin weight ozelligi ile bir liste olusturup elemanlarini topluyoruz
        return sum([present.weight for present in self.presents])


if __name__ == "__main__":
    book = Present("ABC Book", 2)

    print("The name of the present:", book.name)
    print("The weight of the present:", book.weight)
    print("Present:", book)

    # ===============================
    print("\n", "=" * 50, "\n")

    book = Present("ABC Book", 2)

    box = Box()
    box.add_present(book)
    print(box.total_weight())

    cd = Present("Pink Floyd: Dark Side of the Moon", 1)
    box.add_present(cd)
    print(box.total_weight())

    # Çıktı:
    #
    # The name of the present: ABC Book
    # The weight of the present: 2
    # Present: ABC Book (2 kg)
    #
    # ==================================================
    #
    # 2
    # 3
