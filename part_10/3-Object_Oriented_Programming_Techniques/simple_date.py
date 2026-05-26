class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"

    # islem yapabilmek icin gun formatina donusturuyoruz
    def _to_days(self) -> int:
        return self.__day + (self.__month * 30) + (self.__year * 360)

    # karsilastirma operatorleri
    # eşittir
    def __eq__(self, another: "SimpleDate") -> bool:  # type: ignore
        return self._to_days() == another._to_days()

    # eşit değildir
    def __ne__(self, another: "SimpleDate") -> bool:  # type: ignore
        return self._to_days() != another._to_days()

    # küçüktür
    def __lt__(self, another: "SimpleDate") -> bool:
        return self._to_days() < another._to_days()

    # büyüktür
    def __gt__(self, another: "SimpleDate") -> bool:
        return self._to_days() > another._to_days()

    # matematiksel operatorler
    # toplama
    def __add__(self, days_to_add: int) -> "SimpleDate":
        # gun formati ile islem yapiyoruz
        # sondaki -1 gunleri 0 indexli hale getiriyoruz
        total_days = (self._to_days() + days_to_add) - 1

        # gun ay yil formatina geri ceviriyoruz
        new_year = total_days // 360
        remainder = total_days % 360

        new_month = remainder // 30
        new_day = remainder % 30

        return SimpleDate(new_day + 1, new_month + 1, new_year)

    # cikartma
    def __sub__(self, another: "SimpleDate") -> int:
        # iki tarihin gun formatina cevirip aradaki farkin mutlak degerini aliyoruz
        return abs(self._to_days() - another._to_days())


if __name__ == "__main__":
    print("\n", "=" * 10, " Part 1 ", "=" * 10, "\n")
    # part 1
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)
    d3 = SimpleDate(28, 12, 1985)

    print(d1)
    print(d2)
    print(d1 == d2)
    print(d1 != d2)
    print(d1 == d3)
    print(d1 < d2)
    print(d1 > d2)

    # ===============================================
    print("\n", "=" * 10, " Part 2 ", "=" * 10, "\n")
    # part 2
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)

    d3 = d1 + 3
    d4 = d2 + 400

    print(d1)
    print(d2)
    print(d3)
    print(d4)

    # ===============================================
    print("\n", "=" * 10, " Part 3 ", "=" * 10, "\n")
    # part 3
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2 - d1)
    print(d1 - d2)
    print(d1 - d3)

    # Çıktı:
    #
    #
    # ==========  Part 1  ==========
    #
    # 4.10.2020
    # 28.12.1985
    # False
    # True
    # False
    # False
    # True
    #
    # ==========  Part 2  ==========
    #
    # 4.10.2020
    # 28.12.1985
    # 7.11.2020
    # 8.3.1987
    #
    # ==========  Part 3  ==========
    #
    # 28
    # 28
    # 12516
