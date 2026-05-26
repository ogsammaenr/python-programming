class SuperHero:
    def __init__(self, name: str, superpowers: str):
        self.name = name
        self.superpowers = superpowers

    def __str__(self):
        return f"{self.name}, superpowers: {self.superpowers}"


class SuperGroup:
    def __init__(self, name: str, location: str):
        # protected ozelikler
        self._name = name
        self._location = location
        self._members = []

    # Getter
    @property
    def name(self) -> str:
        return self._name

    # Getter
    @property
    def location(self) -> str:
        return self._location

    def add_member(self, hero: SuperHero):
        self._members.append(hero)

    def print_group(self):
        # grup bilgileri
        print(f"{self._name}, {self._location}")
        print("Members:")

        # grup icindeki uyelerin bilgileri
        for hero in self._members:
            print(f"{hero.name}, superpowers: {hero.superpowers}")


# Test Alanı
if __name__ == "__main__":
    superperson = SuperHero("SuperPerson", "Superspeed, superstrength")
    invisible = SuperHero("Invisible Inca", "Invisibility")
    revengers = SuperGroup("Revengers", "Emerald City")

    revengers.add_member(superperson)
    revengers.add_member(invisible)
    revengers.print_group()

    # Çıktı:
    #
    # Revengers, Emerald City
    # Members:
    # SuperPerson, superpowers: Superspeed, superstrength
    # Invisible Inca, superpowers: Invisibility
