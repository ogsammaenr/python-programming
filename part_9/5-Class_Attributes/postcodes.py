class Postcodes:
    postcodes = {
        "Helsinki": "00100",
        "Turku": "20100",
        "Tampere": "33100",
        "Rovaniemi": "96100",
        "Oulu": "90100",
    }

    def __init__(self, name: str, population: int):

        self.name = name
        self.population = population


# Test Alanı (Yapay zeka tarafından oluşturuldu. Soruda bulunmuyor)
if __name__ == "__main__":
    print("--- 1. Sınıf Değişkeni (Class Variable) Testi ---")
    # Nesne (instance) oluşturmadan direkt sınıf üzerinden sözlüğe erişiyoruz
    print("Helsinki Posta Kodu:", Postcodes.postcodes["Helsinki"])
    print("Oulu Posta Kodu:", Postcodes.postcodes["Oulu"])
    print("Tüm Sözlük:", Postcodes.postcodes)
    print("-" * 40)

    print("\n--- 2. Nesne Değişkeni (Instance Variable) Testi ---")
    # İki farklı şehir nesnesi oluşturuyoruz
    city1 = Postcodes("Helsinki", 650000)
    city2 = Postcodes("Turku", 190000)

    # Nesnelerin kendilerine has özelliklerini yazdırıyoruz
    print(f"Şehir 1: {city1.name}, Nüfus: {city1.population}")
    print(f"Şehir 2: {city2.name}, Nüfus: {city2.population}")
    print("-" * 40)

    print("\n--- 3. Nesne Üzerinden Sınıf Değişkenine Erişim ---")
    # Bir nesne üzerinden de ortak sınıf değişkenine erişebilirsin
    print(f"{city1.name} şehrinin posta kodu: {city1.postcodes[city1.name]}")
    print(f"{city2.name} şehrinin posta kodu: {city2.postcodes[city2.name]}")

    # Çıktı:
    #
    # --- 1. Sınıf Değişkeni (Class Variable) Testi ---
    # Helsinki Posta Kodu: 00100
    # Oulu Posta Kodu: 90100
    # Tüm Sözlük: {'Helsinki': '00100', 'Turku': '20100', 'Tampere': '33100', 'Rovaniemi': '96100', 'Oulu': '90100'}
    # ----------------------------------------
    #
    # --- 2. Nesne Değişkeni (Instance Variable) Testi ---
    # Şehir 1: Helsinki, Nüfus: 650000
    # Şehir 2: Turku, Nüfus: 190000
    # ----------------------------------------
    #
    # --- 3. Nesne Üzerinden Sınıf Değişkenine Erişim ---
    # Helsinki şehrinin posta kodu: 00100
    # Turku şehrinin posta kodu: 20100
