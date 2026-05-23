class NumberStats:
    def __init__(self):
        self.numbers = 0
        # kaç adet sayı eklendiğini bulabilmek için bir sayac olusturuyoruz
        self.count = 0

    def add_number(self, number: int):
        self.numbers += number
        # sayiyi eklerken sayaci arttiriyoruz
        self.count += 1

    def count_numbers(self):
        return self.count

    def get_sum(self):
        # numbers degiskeni zaten toplam degeri tutuyor
        return self.numbers

    def average(self):
        # ortalama = sayilarin toplami / sayilarin adeti
        return self.numbers / self.count


# Test Alanı
if __name__ == "__main__":
    # soruda istendigi gibi üç nesne oluşturarak tek ve çift sayıları ayırıyoruz
    stats_all = NumberStats()
    stats_odd = NumberStats()
    stats_even = NumberStats()

    print("Please type in integer numbers:")
    print("(Exit = -1)")
    while True:
        x = int(input())

        if x == -1:
            break

        if x % 2 == 0:
            stats_even.add_number(x)
        else:
            stats_odd.add_number(x)

        stats_all.add_number(x)
    print(" ")
    print(f"Sum of numbers: {stats_all.get_sum()}")
    print(f"Mean of numbers: {stats_all.average()}")
    print(f"Sum of even numbers: {stats_even.get_sum()}")
    print(f"Sum of odd numbers: {stats_odd.get_sum()}")

    # Çıkŧı: (girdiler = [ 4, 2, 5, 2, -1])
    #
    # Please type in integer numbers:
    # (Exit = -1)
    # 4
    # 2
    # 5
    # 2
    # -1
    #
    # Sum of numbers: 13
    # Mean of numbers: 3.25
    # Sum of even numbers: 8
    # Sum of odd numbers: 5
