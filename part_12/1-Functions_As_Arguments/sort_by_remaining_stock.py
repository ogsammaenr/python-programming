def sort_by_remaining_stock(items: list) -> list:
    # item tuple inin 2. elemani ile siralama yapip donduruyoruz
    return sorted(items, key=lambda item: item[2])


# Test Alanı
if __name__ == "__main__":
    products = [
        ("banana", 5.95, 12),
        ("apple", 3.95, 3),
        ("orange", 4.50, 2),
        ("watermelon", 4.95, 22),
    ]

    for product in sort_by_remaining_stock(products):
        print(f"{product[0]} {product[2]} pcs")

    # Çıktı:
    #
    # orange 2 pcs
    # apple 3 pcs
    # banana 12 pcs
    # watermelon 22 pcs
