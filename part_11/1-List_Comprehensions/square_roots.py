def square_roots(numbers: list):
    # numbers listesindeki her number icin number ** 0.5(number ^ 1/2 yani karekok) islemini yaparak yeni bir liste olustur
    return [number**0.5 for number in numbers]


if __name__ == "__main__":
    lines = square_roots([1, 2, 3, 4])
    for line in lines:
        print(line)

    # Çıktı:
    #
    # 1.0
    # 1.4142135623730951
    # 1.7320508075688772
    # 2.0
