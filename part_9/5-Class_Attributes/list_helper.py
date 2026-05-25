class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        if not my_list:
            return None
        # listedeki elemanlarin sayisinin en fazlasini aliyoruz
        return max(my_list, key=my_list.count)

    @classmethod
    def doubles(cls, my_list: list) -> int:
        if not my_list:
            return 0

        # listedeki sayisi 2den fazla olan elemanlarin sayisini donduruyoruz
        # set() kullanmak ayni elemanlarin birden fazla kez kullanilmasini engelliyor
        return len([item for item in set(my_list) if my_list.count(item) >= 2])


# Test Alanı
if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))

    # Çıktı:
    #
    # 5
    # 3
