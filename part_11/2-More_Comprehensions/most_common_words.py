def most_common_words(filename: str, lower_limit: int):
    # dosyayi okuyoruz
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # noktalama isaretlerini metinden temizliyoruz
    for p in ".,!?;:-()[]\"'’“_*":
        content = content.replace(p, "")

    # kelimeleri ayiriyoruz
    all_words = content.split()

    # all_words listesindeki limitten fazla bulunan kelimeleri (kelime : adet) formatinda bir sozluk olusturuyoruz
    return {
        word: all_words.count(word)
        for word in all_words
        if all_words.count(word) >= lower_limit
    }


# Test Alanı ( yapay zeka tarafindan oluşturuldu. )
if __name__ == "__main__":
    # 1. Test için sorudaki örnek metni tanımlıyoruz
    ornek_metin = """List comprehension is an elegant way to define and create lists based on existing lists.
List comprehension is generally more compact and faster than normal functions and loops for creating list.
However, we should avoid writing very long list comprehensions in one line to ensure that code is user-friendly.
Remember, every list comprehension can be rewritten in for loop, but every for loop can’t be rewritten in the form of list comprehension."""

    # 2. Kodun hata vermemesi için geçici bir "comprehensions.txt" dosyası oluşturuyoruz
    with open("comprehensions.txt", "w", encoding="utf-8") as f:
        f.write(ornek_metin)

    # 3. Yazdığımız fonksiyonu test ediyoruz
    print("--- Fonksiyon Çıktısı ---")
    sonuc = most_common_words("comprehensions.txt", 3)
    print(sonuc)

    # Çıktı:
    #
    # --- Fonksiyon Çıktısı ---
    # {'comprehension': 4, 'is': 3, 'and': 3, 'for': 3, 'list': 4, 'in': 3}
