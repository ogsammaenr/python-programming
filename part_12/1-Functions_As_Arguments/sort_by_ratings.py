def sort_by_ratings(items: list) -> list:
    # rating verisine gore verileri tersten siraliyoruz
    return sorted(items, key=lambda show: show["rating"], reverse=True)


# Test Alanı
if __name__ == "__main__":
    shows = [
        {"name": "Dexter", "rating": 8.6, "seasons": 9},
        {"name": "Friends", "rating": 8.9, "seasons": 10},
        {"name": "Simpsons", "rating": 8.7, "seasons": 32},
    ]

    print("Rating according to IMDB")
    for show in sort_by_ratings(shows):
        print(f"{show['name']}  {show['rating']}")

    # Çıktı:
    #
    # Rating according to IMDB
    # Friends  8.9
    # Simpsons  8.7
    # Dexter  8.6
