class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"


def sort_by_length(routes: list) -> list:
    # route nesnelerinin length verilerine gore tersten siraliyoruz
    return sorted(routes, key=lambda route: route.length, reverse=True)


def sort_by_difficulty(routes: list) -> list:
    # route nesnelerini ilk olarak grade verisine gore ikinci olarak length verisine gore tersten siraliyoruz
    # ikinci filtre esitlik durumunda calisir
    return sorted(routes, key=lambda route: (route.grade, route.length), reverse=True)


if __name__ == "__main__":
    print("\n", "=" * 20, " Part 1 ", "=" * 20, "\n")

    route1 = ClimbingRoute("Edge", 38, "6A+")
    route2 = ClimbingRoute("Smooth operator", 11, "7A")
    route3 = ClimbingRoute("Synchro", 14, "8C+")

    print(route1)
    print(route2)
    print(route3.name, route3.length, route3.grade)

    print("\n", "=" * 20, " Part 2 ", "=" * 20, "\n")

    r1 = ClimbingRoute("Edge", 38, "6A+")
    r2 = ClimbingRoute("Smooth operator", 11, "7A")
    r3 = ClimbingRoute("Synchro", 14, "8C+")
    r4 = ClimbingRoute("Small steps", 12, "6A+")

    routes = [r1, r2, r3, r4]

    for route in sort_by_length(routes):
        print(route)

    print("\n", "=" * 20, " Part 3 ", "=" * 20, "\n")

    r1 = ClimbingRoute("Edge", 38, "6A+")
    r2 = ClimbingRoute("Smooth operator", 11, "7A")
    r3 = ClimbingRoute("Synchro", 14, "8C+")
    r4 = ClimbingRoute("Small steps", 12, "6A+")

    routes = [r1, r2, r3, r4]
    for route in sort_by_difficulty(routes):
        print(route)

    # Çıktı:
    #
    #  ====================  Part 1  ====================
    #
    # Edge, length 38 metres, grade 6A+
    # Smooth operator, length 11 metres, grade 7A
    # Synchro 14 8C+
    #
    # ====================  Part 2  ====================
    #
    # Edge, length 38 metres, grade 6A+
    # Synchro, length 14 metres, grade 8C+
    # Small steps, length 12 metres, grade 6A+
    # Smooth operator, length 11 metres, grade 7A
    #
    # ====================  Part 3  ====================
    #
    # Synchro, length 14 metres, grade 8C+
    # Smooth operator, length 11 metres, grade 7A
    # Edge, length 38 metres, grade 6A+
    # Small steps, length 12 metres, grade 6A+
