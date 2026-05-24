class RealProperty:
    def __init__(self, rooms: int, square_metres: int, price_per_sqm: int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

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


if __name__ == "__main__":
    central_studio = RealProperty(1, 16, 5500)
    downtown_two_bedroom = RealProperty(2, 38, 4200)
    suburbs_three_bedroom = RealProperty(3, 78, 2500)

    print(central_studio.bigger(downtown_two_bedroom))
    print(suburbs_three_bedroom.bigger(downtown_two_bedroom))

    # ========================================================
    print("\n", "=" * 50, "\n")

    central_studio = RealProperty(1, 16, 5500)
    downtown_two_bedroom = RealProperty(2, 38, 4200)
    suburbs_three_bedroom = RealProperty(3, 78, 2500)

    print(central_studio.price_difference(downtown_two_bedroom))
    print(suburbs_three_bedroom.price_difference(downtown_two_bedroom))

    # ========================================================
    print("\n", "=" * 50, "\n")

    central_studio = RealProperty(1, 16, 5500)
    downtown_two_bedroom = RealProperty(2, 38, 4200)
    suburbs_three_bedroom = RealProperty(3, 78, 2500)

    print(central_studio.more_expensive(downtown_two_bedroom))
    print(suburbs_three_bedroom.more_expensive(downtown_two_bedroom))

    # Çıktı:
    #
    # False
    # True
    #
    # ==================================================
    #
    # 71600
    # 35400
    #
    # ==================================================
    #
    # False
    # True
