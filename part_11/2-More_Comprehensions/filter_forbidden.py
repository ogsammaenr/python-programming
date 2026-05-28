def filter_forbidden(string: str, forbidden: str):
    # metindeki her karakter icin forbidden metninde olmayanlar ile yeni bir liste olusturuyoruz
    # ve bu listenin elemanlarini birlestiriyoruz
    return "".join([char for char in string if char not in forbidden])


if __name__ == "__main__":
    sentence = "Once! upon, a time: there was a python!??!?!"
    filtered = filter_forbidden(sentence, "!?:,.")
    print(filtered)

    # Çıktı:
    #
    # Once upon a time there was a python
