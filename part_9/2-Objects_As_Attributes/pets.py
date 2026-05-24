class Pet:
    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed


class Person:
    def __init__(self, name: str, pet: Pet):
        self.name = name
        self.pet = pet

    def __str__(self):
        return f"{self.name}, whose pal is {self.pet.name}, a {self.pet.breed}"


# Test Alanı
if __name__ == "__main__":
    hulda = Pet("Hulda", "mixed-breed dog")

    # pet nesnesini person nesnesini olustururken referans veriyoruz
    levi = Person("Levi", hulda)

    print(levi)

    # Çıktı:
    #
    # Levi, whose pal is Hulda, a mixed-breed dog
