class Car:
    def __init__(self):
        ## __ private anlamina geliyor ve dişarıdan erışimi engelliyor
        self.__petrol = 0
        self.__odometer = 0

    def fill_up(self):
        self.__petrol = 60

    def drive(self, km: int):
        # petrol verisine gore arabanin gidebilecegi gercek mesefeyi hesapliyoruz
        drive_distance = min(km, self.__petrol)

        self.__odometer += drive_distance
        self.__petrol -= drive_distance

    def __str__(self):
        # soruda istenen cikti formati
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__petrol} litres"


# Test Alanı
if __name__ == "__main__":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)

    # Çıktı:
    #
    # Car: odometer reading 0 km, petrol remaining 0 litres
    # Car: odometer reading 0 km, petrol remaining 60 litres
    # Car: odometer reading 20 km, petrol remaining 40 litres
    # Car: odometer reading 60 km, petrol remaining 0 litres
    # Car: odometer reading 60 km, petrol remaining 0 litres
    # Car: odometer reading 60 km, petrol remaining 60 litres
