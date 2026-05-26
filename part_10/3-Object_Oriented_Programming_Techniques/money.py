class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        # 10 dan kucuk olan centlerin basina 0 koyuyoruz (5 cent = 0.05 eur)
        cents = "0" + str(self.__cents) if self.__cents < 10 else str(self.__cents)
        return f"{self.__euros}.{cents} eur"

    # parayi cent formatina cevirir
    def _to_cents(self) -> int:
        return self.__euros * 100 + self.__cents

    # karsilastirma operatorleri
    # eşittir
    def __eq__(self, another: "Money") -> bool:  # type: ignore
        return self._to_cents() == another._to_cents()

    # eşit değildir
    def __ne__(self, another: "Money") -> bool:  # type: ignore
        return self._to_cents() != another._to_cents()

    # küçükŧür
    def __lt__(self, another: "Money") -> bool:
        return self._to_cents() < another._to_cents()

    # büyükŧür
    def __gt__(self, another: "Money") -> bool:
        return self._to_cents() > another._to_cents()

    # matematiksel operatorler
    def __add__(self, another: "Money") -> "Money":
        # paralari cent formatina cevirip topluyoruz
        total_cents = self._to_cents() + another._to_cents()

        # tekrardan euro formatina ceviriyoruz
        new_euros = total_cents // 100
        new_cents = total_cents % 100

        # yeni degerler ile geriye yeni bir nesne donduruyoruz
        return Money(new_euros, new_cents)

    def __sub__(self, another: "Money") -> "Money":
        # paralari cent formatina ceviriyoruz
        total_cents_self = self._to_cents()
        total_cents_another = another._to_cents()

        # para negatif kalamaz!
        if total_cents_self < total_cents_another:
            raise ValueError("a negative result is not allowed")

        # cent formatinda islemi yapiyoruz
        remaining_cents = total_cents_self - total_cents_another

        # yeniden euro formatina donduruyoruz
        new_euros = remaining_cents // 100
        new_cents = remaining_cents % 100

        # yeni degerler ile geriye yeni bir nesne donduruyoruz
        return Money(new_euros, new_cents)


if __name__ == "__main__":
    print("\n", "=" * 10, " Part 1 ", "=" * 10, "\n")
    # part 1
    e1 = Money(4, 10)
    e2 = Money(2, 5)  # two euros and five cents

    print(e1)
    print(e2)

    # ==========================================
    print("\n", "=" * 10, " Part 2 ", "=" * 10, "\n")

    # part 2
    e1 = Money(4, 10)
    e2 = Money(2, 5)
    e3 = Money(4, 10)

    print(e1)
    print(e2)
    print(e3)
    print(e1 == e2)
    print(e1 == e3)

    # ==========================================
    print("\n", "=" * 10, " Part 3 ", "=" * 10, "\n")

    # part 3
    e1 = Money(4, 10)
    e2 = Money(2, 5)

    print(e1 != e2)
    print(e1 < e2)
    print(e1 > e2)

    # ==========================================
    print("\n", "=" * 10, " Part 4 ", "=" * 10, "\n")

    # part 4
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2 - e1

    # ==========================================
    print("\n", "=" * 10, " Part 5 ", "=" * 10, "\n")

    # part 5
    print(e1)
    e1.euros = 1000  # type: ignore
    print(e1)

    # Çıktı:
    #
    # ==========  Part 1  ==========
    #
    # 4.10 eur
    # 2.05 eur
    #
    # ==========  Part 2  ==========
    #
    # 4.10 eur
    # 2.05 eur
    # 4.10 eur
    # False
    # True
    #
    # ==========  Part 3  ==========
    #
    # True
    # False
    # True
    #
    # ==========  Part 4  ==========
    #
    # 7.00 eur
    # 1.10 eur
    # Traceback (most recent call last):
    # File "/home/excalibur/WorkSpace/projects/python-programming/part_10/3-Object_Oriented_Programming_Techniques/money.py", line 107, in <module>
    #     e5 = e2 - e1
    #         ~~~^~~~
    # File "/home/excalibur/WorkSpace/projects/python-programming/part_10/3-Object_Oriented_Programming_Techniques/money.py", line 47, in __sub__
    #     raise ValueError("a negative result is not allowed")
    # ValueError: a negative result is not allowed
    #
