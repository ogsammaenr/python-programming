def begin_with_vowel(words: list):
    # words listesindeki her word icin ilk harfinin sesli olup olmadigini kontrol ederek yeni bir liste olusturuyoruz
    return [word for word in words if word[0].lower() in "aeiou"]


if __name__ == "__main__":
    word_list = ["automobile", "motorbike", "Animal", "cat", "Dog", "APPLE", "orange"]
    for vowelled in begin_with_vowel(word_list):
        print(vowelled)

    # Çıkti:
    #
    # automobile
    # Animal
    # APPLE
    # orange
