def sort_by_seasons(items: list) -> list:
    # sozlukteki seasons verisine gore siralama yapip donduruyoruz
    return sorted(items, key=lambda item: item["seasons"])


# Test Alanı
if __name__ == "__main__":
    shows = [
        {"name": "Dexter", "rating": 8.6, "seasons": 9},
        {"name": "Friends", "rating": 8.9, "seasons": 10},
        {"name": "Simpsons", "rating": 8.7, "seasons": 32},
    ]

    for show in sort_by_seasons(shows):
        print(f"{show['name']} {show['seasons']} seasons")

    # Çıktı:
    #
    # Dexter 9 seasons
    # Friends 10 seasons
    # Simpsons 32 seasons
