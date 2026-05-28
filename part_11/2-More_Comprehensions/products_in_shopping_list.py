class ShoppingList:
    def __init__(self):
        self.products = []
        self.n = 0

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def number_of_items(self):
        return len(self.products)

    def __iter__(self):
        # baslangicta indexi sifirliyoruz
        self.n = 0
        return self

    def __next__(self):
        # sayac liste boyutuna ulastiysa bitiriyoruz
        if self.n >= len(self.products):
            raise StopIteration

        # sonraki urune geciyoruz
        current_product = self.products[self.n]
        self.n += 1

        return current_product


def products_in_shopping_list(shopping_list: ShoppingList, amount: int):
    # shopping_list nesnesi icindeki isim, adet verilerinden adet amountdan buyuk olanlarin isim verileri ile liste olusturuyoruz
    return [isim for isim, adet in shopping_list if adet >= amount]


if __name__ == "__main__":
    my_list = ShoppingList()
    my_list.add("bananas", 10)
    my_list.add("apples", 5)
    my_list.add("alcohol free beer", 24)
    my_list.add("pineapple", 1)

    print("the shopping list contains at least 8 of the following items:")
    for product in products_in_shopping_list(my_list, 8):
        print(product)

    # Çıktı:
    #
    # the shopping list contains at least 8 of the following items:
    # bananas
    # alcohol free beer
