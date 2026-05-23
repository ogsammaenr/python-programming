class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres

        # oylamalari saklamak icin liste
        # liste yerine toplam puani ve oylama sayisini ayri ayri saklayarak da ayni mantik kurulabilr
        self.ratings = []

    def rate(self, rating: int):
        self.ratings.append(rating)

    def get_rating(self):
        return sum(self.ratings) / len(self.ratings)

    def __str__(self):
        # genre listesini stringe donustur
        genres_str = ", ".join(self.genres)

        # eger hic oylama yoksa 'no rating' olarak ata var ise oylama sayisini ve puan ortalamasini ata
        rating = (
            "no rating"
            if len(self.ratings) == 0
            else f"{len(self.ratings)} ratings, average {sum(self.ratings) / len(self.ratings)}"
        )

        # butun bilgileri birlestir
        return f" {self.title} ({self.seasons})\n genres: {genres_str}\n {rating}"


def minimum_grade(rating: float, series_list: list):
    return [series for series in series_list if series.get_rating() >= rating]


def includes_genre(genre: str, series_list: list):
    return [series for series in series_list if genre in series.genres]


# Test Alanı
if __name__ == "__main__":
    dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    dexter.rate(4)
    dexter.rate(5)
    dexter.rate(5)
    dexter.rate(3)
    dexter.rate(0)
    print(dexter)

    print("\n", "=" * 50, "\n")

    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print(" ")

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)

    # Çıktı:
    #
    # Dexter (8)
    # genres: Crime, Drama, Mystery, Thriller
    # 5 ratings, average 3.4
    #
    # ==================================================
    #
    # a minimum grade of 4.5:
    # Dexter
    #
    # genre Comedy:
    # South Park
    # Friends
