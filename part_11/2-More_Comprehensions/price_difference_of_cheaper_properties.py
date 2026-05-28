class RealProperty:
    def __init__(
        self, rooms: int, square_metres: int, price_per_sqm: int, description: str
    ):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm
        self.description = description

    def bigger(self, compared_to: "RealProperty"):
        # nesnenin metrekaresi ile karsilastirilan nesnenin metrekaresini karsilastir
        return self.square_metres > compared_to.square_metres

    def price_difference(self, compared_to: "RealProperty"):
        # iki nesnenin de toplam fiyatini hesapla
        self_total_price = self.square_metres * self.price_per_sqm
        compared_total_price = compared_to.square_metres * compared_to.price_per_sqm

        # aradaki farkın mutlak degerini al ve dondür
        return abs(self_total_price - compared_total_price)

    def more_expensive(self, compared_to: "RealProperty"):
        # toplam fiyatlari hesapla ve karsilastir
        my_total_price = self.square_metres * self.price_per_sqm
        compared_total_price = compared_to.square_metres * compared_to.price_per_sqm

        return my_total_price > compared_total_price


def cheaper_properties(properties: list, reference: RealProperty):
    # properties listesindeki referanstan pahali olan nesneleri bulup elemanlari (property , fiyat farki) formatinda olan bir liste olusturuyoruz
    return [
        (property, reference.price_difference(property))
        for property in properties
        if reference.more_expensive(property)
    ]


# Test Alanı
if __name__ == "__main__":
    a1 = RealProperty(1, 16, 5500, "Central studio")
    a2 = RealProperty(2, 38, 4200, "Two bedrooms downtown")
    a3 = RealProperty(3, 78, 2500, "Three bedrooms in the suburbs")
    a4 = RealProperty(6, 215, 500, "Farm in the middle of nowhere")
    a5 = RealProperty(4, 105, 1700, "Loft in a small town")
    a6 = RealProperty(25, 1200, 2500, "Countryside mansion")

    properties = [a1, a2, a3, a4, a5, a6]

    print(f"cheaper options when compared to {a3.description}:")
    for item in cheaper_properties(properties, a3):
        print(f"{item[0].description:35} price difference {item[1]} euros")

    # Çıktı:
    #
    # cheaper options when compared to Three bedrooms in the suburbs:
    # Central studio                      price difference 107000 euros
    # Two bedrooms downtown               price difference 35400 euros
    # Farm in the middle of nowhere       price difference 87500 euros
    # Loft in a small town                price difference 16500 euros
