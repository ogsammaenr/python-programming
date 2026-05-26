class MagicPotion:
    def __init__(self, name: str):
        self._name = name
        self._ingredients = []

    def add_ingredient(self, ingredient: str, amount: float):
        self._ingredients.append((ingredient, amount))

    def print_recipe(self):
        print(f"{self._name}:")
        for ingredient, amount in self._ingredients:
            print(f"{ingredient} {amount} grams")


class SecretMagicPotion(MagicPotion):
    def __init__(self, name: str, password: str):
        # ata sinifin constructor metodu
        super().__init__(name)

        self.__password = password

    def add_ingredient(self, ingredient: str, amount: float, password: str):  # type: ignore
        if password != self.__password:
            raise ValueError("Wrong password!")

        super().add_ingredient(ingredient, amount)

    def print_recipe(self, password: str):  # type: ignore
        if password != self.__password:
            raise ValueError("Wrong password!")

        # ata sinifdaki yazdirma metodu
        super().print_recipe()


# Test Alanı
if __name__ == "__main__":
    diminuendo = SecretMagicPotion("Diminuendo maximus", "hocuspocus")
    diminuendo.add_ingredient("Toadstool", 1.5, "hocuspocus")
    diminuendo.add_ingredient("Magic sand", 3.0, "hocuspocus")
    diminuendo.add_ingredient("Frogspawn", 4.0, "hocuspocus")
    diminuendo.print_recipe("hocuspocus")

    diminuendo.print_recipe("pocushocus")  # WRONG password!

    # Çıkŧı:
    #
    # Diminuendo maximus:
    # Toadstool 1.5 grams
    # Magic sand 3.0 grams
    # Frogspawn 4.0 grams
    # Traceback (most recent call last):
    # File "/home/excalibur/WorkSpace/projects/python-programming/part_10/2-Access_Modifiers/secret_magic_potion.py", line 43, in <module>
    #     diminuendo.print_recipe("pocushocus")  # WRONG password!
    #     ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
    # File "/home/excalibur/WorkSpace/projects/python-programming/part_10/2-Access_Modifiers/secret_magic_potion.py", line 30, in print_recipe
    #     raise ValueError("Wrong password!")
    # ValueError: Wrong password!
