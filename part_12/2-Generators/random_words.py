import random


def word_generator(characters: str, length: int, amount: int):
    # for dongusunde _ degisken olusturmadan dongu kurmayi saglar
    for _ in range(amount):
        # characters metninden length kadar rastgele karakterler secerek birlestiriyoruz
        random_word = "".join(
            [characters[random.randint(0, len(characters) - 1)] for _ in range(length)]
        )

        # birlestirilmis kelimeyi gonderiyoruz
        yield random_word


if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)

    # Çıktı:
    #
    # dad
    # gda
    # ede
    # feb
    # gbf
