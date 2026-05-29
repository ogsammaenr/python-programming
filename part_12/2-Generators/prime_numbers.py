def prime_numbers():
    # en kucuk asal sayi olan 2 den basliyoruz
    current = 2

    while True:
        is_prime = True
        # kontrol ettigimiz sayi 2 ile kontrol ettigimiz sayi arasindaki herhangi bir sayiya bolunuyorsa asal degildir
        for i in range(2, current):
            if current % i == 0:
                is_prime = False
                break

        # eger is_prime halen true kaldiysa gonderiyoruz
        if is_prime:
            yield current

        current += 1


if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))

    # Çıktı:
    #
    # 2
    # 3
    # 5
    # 7
    # 11
    # 13
    # 17
    # 19
