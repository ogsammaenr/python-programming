class CheckList:
    def __init__(self, header: str, entries: list):
        self.header = header
        self.entries = entries


class Customer:
    def __init__(self, id: str, balance: float, discount: int):
        self.id = id
        self.balance = balance
        self.discount = discount


class Cable:
    def __init__(self, model: str, length: float, max_speed: int, bidirectional: bool):
        self.model = model
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectional


# Test Alanı
if __name__ == "__main__":
    alinacaklar = CheckList("alisveris listesi", ["elma", "armut", "domat"])
    print(alinacaklar.header, alinacaklar.entries)

    musteri1 = Customer("ID1", 1000.10, 15)
    musteri2 = Customer("ID2", 300.0, 30)
    print(f"Idler: {musteri1.id} , {musteri2.id}")

    kablo = Cable("uzun", 10, 5000, False)
    print(f"kablo cift yonlu mu ? \n {kablo.bidirectional}")

    # Çıktı:
    #
    # alisveris listesi ['elma', 'armut', 'domat']
    # Idler: ID1 , ID2
    # kablo cift yonlu mu ?
    # False
