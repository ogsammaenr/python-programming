class Car:
    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed


def fastest_car(cars: list):
    # cars listesindeki arabalarin hizlarina gore en buyuk Car nesnesini bulup adini dondur
    return max(cars, key=lambda car: car.speed).name


# Test Alanı
if __name__ == "__main__":
    car1 = Car("Saab", 195)
    car2 = Car("Lada", 110)
    car3 = Car("Ferrari", 280)
    car4 = Car("Trabant", 85)

    cars = [car1, car2, car3, car4]
    print(fastest_car(cars))

    # Çıktı:
    #
    # Ferrari
