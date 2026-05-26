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


# Test Alanı
if __name__ == "__main__":
    shopping_list = ShoppingList()
    shopping_list.add("bananas", 10)
    shopping_list.add("apples", 5)
    shopping_list.add("pineapple", 1)

    for product in shopping_list:
        print(f"{product[0]}: {product[1]} units")

    # Çıktı:
    #
    # bananas: 10 units
    # apples: 5 units
    # pineapple: 1 units
