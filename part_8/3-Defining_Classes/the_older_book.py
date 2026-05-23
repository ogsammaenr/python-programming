from book import Book


def older_book(book1: Book, book2: Book):

    # book2 daha yaşlı ise
    if book1.year < book2.year:
        print(f"{book1.name} is older, it was published in {book1.year}")

    # book1 daha yaşli ise
    elif book2.year < book1.year:
        print(f"{book2.name} is older, it was published in {book2.year}")

    # iki kitabin yaşları eşit ise
    else:
        print(f"{book1.name} and {book2.name} were published in {book1.year}")


# Test Alanı
if __name__ == "__main__":
    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
    norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

    older_book(python, everest)
    older_book(python, norma)

    # Çıktı:
    #
    # High Adventure is older, it was published in 1956
    # Fluent Python and Norma were published in 2015
