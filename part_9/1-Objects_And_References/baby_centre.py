class Person:
    def __init__(self, name: str, age: int, height: int, weight: int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


class BabyCentre:
    def __init__(self):
        self.total_weigh_ins = 0

    def weigh(self, person: Person):
        self.total_weigh_ins += 1
        return person.weight

    def feed(self, person: Person):
        person.weight += 1

    def weigh_ins(self):
        return self.total_weigh_ins


# Test Alanı
if __name__ == "__main__":
    baby_centre = BabyCentre()

    eric = Person("Eric", 1, 110, 7)
    peter = Person("Peter", 33, 176, 85)

    print(f"{eric.name} weighs {baby_centre.weigh(eric)} kg")
    print(f"{peter.name} weighs {baby_centre.weigh(peter)} kg")
    print()

    baby_centre.feed(eric)
    baby_centre.feed(eric)
    baby_centre.feed(eric)

    print(f"{eric.name} weighs {baby_centre.weigh(eric)} kg")
    print(f"{peter.name} weighs {baby_centre.weigh(peter)} kg")

    print("\n", "=" * 50, "\n")

    eric1 = Person("Eric", 1, 110, 7)

    print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

    baby_centre.weigh(eric1)
    baby_centre.weigh(eric1)

    print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

    baby_centre.weigh(eric1)
    baby_centre.weigh(eric1)
    baby_centre.weigh(eric1)
    baby_centre.weigh(eric1)

    print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

    # Çıktı:
    #
    # Eric weighs 7 kg
    # Peter weighs 85 kg
    #
    # Eric weighs 10 kg
    # Peter weighs 85 kg
    #
    # ==================================================
    #
    # Total number of weigh-ins is 4
    # Total number of weigh-ins is 6
    # Total number of weigh-ins is 10
