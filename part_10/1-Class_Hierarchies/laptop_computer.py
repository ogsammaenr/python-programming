class Computer:
    def __init__(self, model: str, speed: int):
        self.__model = model
        self.__speed = speed

    @property
    def model(self) -> str:
        return self.__model

    @property
    def speed(self) -> int:
        return self.__speed


# Computer sinifini miras alan yeni bir sinif olusturuyoruz
class LaptopComputer(Computer):
    def __init__(self, model: str, speed: int, weight: int):
        # ust sinifin constructor metodunu cagiriyoruz
        super().__init__(model, speed)

        # cocuk sinifa ozel agirlik verisini burada tanimliyoruz
        self.__weight = weight

    @property
    def weight(self) -> int:
        return self.__weight

    def __str__(self):
        return f"{self.model}, {self.speed} MHz, {self.weight} kg"


if __name__ == "__main__":
    laptop = LaptopComputer("NoteBook Pro15", 1500, 2)
    print(laptop)

    # Çıktı:
    #
    # NoteBook Pro15, 1500 MHz, 2 kg
