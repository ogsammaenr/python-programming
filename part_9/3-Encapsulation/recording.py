class Recording:
    def __init__(self, length: int):
        # nesne olusturulurken setter metodunu çağırıyoruz
        self.length = length

    @property
    def length(self) -> int:
        return self.__lenght

    @length.setter
    def length(self, amount: int):
        # amount parametresinin sıfırdan büyük olduğunu kontrol ediyoruz
        if amount < 0:
            raise ValueError("The lenght cannot below zero.")

        self.__lenght = amount


# Test Alanı
if __name__ == "__main__":
    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)

    # Çıkŧı:
    #
    # 43
    # 44
