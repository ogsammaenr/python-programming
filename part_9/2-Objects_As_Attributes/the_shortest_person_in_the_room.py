class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height})"


class Room:
    def __init__(self):
        # person nesnelerini tutacak nesne
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        return len(self.persons) == 0

    def print_contents(self):
        # toplam insan sayısı ve toplam boy hesabı
        total_persons = len(self.persons)
        combined_height = sum([person.height for person in self.persons])

        print(
            f"There are {total_persons} persons in the room, and their combined height is {combined_height} cm"
        )

        # listedeki butun elemanlari terminale yazdir
        for person in self.persons:
            print(person)

    def shortest(self):
        if self.is_empty():
            return None

        # en kucuk person nesnesini height ozellligine gore bul
        return min(self.persons, key=lambda person: person.height)

    def remove_shortest(self):
        shortest_person = self.shortest()

        # None kontrolu yapip listeden kaldiriyoruz
        if shortest_person is not None:
            self.persons.remove(shortest_person)

        return shortest_person


# Test Alanı
if __name__ == "__main__":
    room = Room()
    print("Is the room empty?", room.is_empty())

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Ally", 166))
    room.add(Person("Nina", 162))
    room.add(Person("Dorothy", 155))

    print("Is the room empty?", room.is_empty())
    room.print_contents()

    # ===============================
    print("\n", "=" * 50, "\n")

    room = Room()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))

    print()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    print()

    room.print_contents()

    # ===============================
    print("\n", "=" * 50, "\n")

    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
