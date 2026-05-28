class LotteryNumbers:
    def __init__(self, week_number: int, numbers: list):
        self.__week_number = week_number
        self.__numbers = numbers

    def number_of_hits(self, numbers: list):
        # numbers listesindeki her number in __numbers listesinde olup olmadigini kontrol edip bir liste olusturuyoruz
        # ve bu listenini uzunlugunu donduruyoruz
        return len([number for number in numbers if number in self.__numbers])

    def hits_in_place(self, numbers: list):
        # numbers listesindeki elemanlar eger __numbers listesinde ise direkt olarak number yok ise -1 olacak sekilde yeni bir liste olusturuyoruz
        return [number if number in self.__numbers else -1 for number in numbers]


if __name__ == "__main__":
    print("\n", "=" * 10, " Part 1 ", "=" * 10, "\n")

    week5 = LotteryNumbers(5, [1, 2, 3, 4, 5, 6, 7])
    my_numbers = [1, 4, 7, 11, 13, 19, 24]
    print(week5.number_of_hits(my_numbers))

    print("\n", "=" * 10, " Part 2 ", "=" * 10, "\n")

    week8 = LotteryNumbers(8, [1, 2, 3, 10, 20, 30, 33])
    my_numbers2 = [1, 4, 7, 10, 11, 20, 30]
    print(week8.hits_in_place(my_numbers2))
