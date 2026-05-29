import re


def is_dotw(my_string: str):
    # sablon :
    # metin Mon, Tue, Wed, Thu, Fri, Sat veya Sun metinlarinden birisi olmasi lazim
    pattern = "^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)$"
    return bool(re.search(pattern, my_string))


def all_vowels(my_string: str):
    # sablon:
    # metin sadece aeiou karakterleri ile olusmasi lazim
    pattern = "^[aeiou]+$"
    return bool(re.search(pattern, my_string))


def time_of_day(my_string: str):
    # sablon:
    # 1. karakter 0 veya 1 ise 2. karakter 0 ile 9 arasinda olmali veya ilk karakter 2 olursa 2. karakter 0 ile 3 arasinda olmali
    # 3. karakter sabit : 4. karakter 0 ile 5 arasinda olmali 5. karakter 0 ile 9 arasinda olmali
    # 6. karakter sabit : 7. karakter 0 ile 5 arasinda olmali 8. karakter 0 ile 9 arasinda olmali
    pattern = "^([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$"
    return bool(re.search(pattern, my_string))


if __name__ == "__main__":
    print("\n", "=" * 20, " Part 1 ", "=" * 20, "\n")

    print(is_dotw("Mon"))
    print(is_dotw("Fri"))
    print(is_dotw("Tui"))

    print("\n", "=" * 20, " Part 2 ", "=" * 20, "\n")

    print(all_vowels("eioueioieoieou"))
    print(all_vowels("autoooo"))

    print("\n", "=" * 20, " Part 3 ", "=" * 20, "\n")

    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))

    # Çıktı:
    #
    #  ====================  Part 1  ====================
    #
    # True
    # True
    # False
    #
    # ====================  Part 2  ====================
    #
    # True
    # False
    #
    # ====================  Part 3  ====================
    #
    # True
    # False
    # True
    # False
