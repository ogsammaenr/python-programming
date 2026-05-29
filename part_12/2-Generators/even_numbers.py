def even_numbers(beginning: int, maximum: int):
    # eger baslangicta sayi cift degilse sonraki cift sayiya geciyoruz
    if beginning % 2 != 0:
        beginning += 1

    while beginning <= maximum:
        # suanki sayiyi gonderip sonraki cift sayiya geciyoruz
        yield beginning
        beginning += 2


# Test Alanı
if __name__ == "__main__":
    numbers = even_numbers(2, 10)
    for number in numbers:
        print(number)

    print("\n===============\n")

    numbers = even_numbers(11, 21)
    for number in numbers:
        print(number)

    # Çıktı:
    #
    # 2
    # 4
    # 6
    # 8
    # 10
    #
    # ===============
    #
    # 12
    # 14
    # 16
    # 18
    # 20
