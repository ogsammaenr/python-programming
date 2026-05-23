# soruda bahsettiği sinif yapisi
class ShoppingList:
    def __init__(self):
        self.__liste = []

    def add(self, name: str, amount: int):
        self.__liste.append([name, amount])

    def number_of_items(self):
        return len(self.__liste)

    def item(self, index: int):
        # Unlike normal Python lists, indexing starts from 1, not 0.
        # dediği için 1 tabanli bir indexleme sistemi kullaniyoruz
        return self.__liste[index - 1][0]

    def amount(self, index: int):
        # ayni sekilde 1 tabanli indexleme kullanioyuruz
        return self.__liste[index - 1][1]


def total_units(my_list: ShoppingList):
    toplam = 0

    # 1 den baslayan index yapisina gore dolasip sayiyoruz
    for i in range(1, my_list.number_of_items() + 1):
        toplam += my_list.amount(i)

    return toplam


# Test Alanı
if __name__ == "__main__":
    my_list = ShoppingList()
    my_list.add("bananas", 10)
    my_list.add("apples", 5)
    my_list.add("pineapple", 1)

    print(total_units(my_list))

    # Çıktı:
    #
    # 16
