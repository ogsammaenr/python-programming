class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"


class ClimbingArea:
    def __init__(self, name: str):
        self.name = name
        self.__routes = []

    def add_route(self, route: ClimbingRoute):
        self.__routes.append(route)

    def routes(self) -> int:
        return len(self.__routes)

    def hardest_route(self) -> ClimbingRoute | None:
        if not self.__routes:
            return None
        # Rotaları alfabetik grade değerine göre sıralayıp en sondakini alıyoruz
        return sorted(self.__routes, key=lambda r: r.grade)[-1]

    def __str__(self):
        return (
            f"{self.name}, {self.routes()} routes, hardest {self.hardest_route().grade}"  # type: ignore
        )


def sort_by_number_of_routes(areas: list) -> list:
    # route nesnelerinin length verilerine gore tersten siraliyoruz
    return sorted(areas, key=lambda area: area.routes())


def sort_by_most_difficult(areas: list) -> list:
    # route nesnelerini ilk olarak grade verisine gore ikinci olarak length verisine gore tersten siraliyoruz
    # ikinci filtre esitlik durumunda calisir
    return sorted(areas, key=lambda area: area.hardest_route().grade, reverse=True)


if __name__ == "__main__":
    ca1 = ClimbingArea("Olhava")
    ca1.add_route(ClimbingRoute("Edge", 38, "6A+"))
    ca1.add_route(ClimbingRoute("Great cut", 36, "6B"))
    ca1.add_route(ClimbingRoute("Swedish route", 42, "5+"))

    ca2 = ClimbingArea("Nummi")
    ca2.add_route(ClimbingRoute("Synchro", 14, "8C+"))

    ca3 = ClimbingArea("Nalkkila slab")
    ca3.add_route(ClimbingRoute("Small steps", 12, "6A+"))
    ca3.add_route(ClimbingRoute("Smooth operator", 11, "7A"))
    ca3.add_route(ClimbingRoute("Piggy not likey", 12, "6B+"))
    ca3.add_route(ClimbingRoute("Orchard", 8, "6A"))

    print(ca1)
    print(ca3.name, ca3.routes())
    print(ca3.hardest_route())

    print("\n", "=" * 20, " Part 1 ", "=" * 20, "\n")

    # ca1, ca2 and ca3 declared as above
    areas = [ca1, ca2, ca3]
    for area in sort_by_number_of_routes(areas):
        print(area)

    print("\n", "=" * 20, " Part 2 ", "=" * 20, "\n")

    # ca1, ca2 and ca3 declared as above
    areas = [ca1, ca2, ca3]
    for area in sort_by_most_difficult(areas):
        print(area)

    # Çıktı:
    #
    # Olhava, 3 routes, hardest 6B
    # Nalkkila slab 4
    # Smooth operator, length 11 metres, grade 7A
    #
    # ====================  Part 1  ====================
    #
    # Nummi, 1 routes, hardest 8C+
    # Olhava, 3 routes, hardest 6B
    # Nalkkila slab, 4 routes, hardest 7A
    #
    # ====================  Part 2  ====================
    #
    # Nummi, 1 routes, hardest 8C+
    # Nalkkila slab, 4 routes, hardest 7A
    # Olhava, 3 routes, hardest 6B
