class Rectangle:
    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"rectangle {self.__width}x{self.__height}"


class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)

    def __str__(self):
        # soruda kare sinifinda baska veri tutulmasi istenmedigi icin kenar uzunlugunu
        # alanin karekokunu alarak buluyoruz
        side = int(self.area() ** 0.5)
        return f"square {side}x{side}"


# Test Alanı
if __name__ == "__main__":
    rectangle = Rectangle(2, 3)
    print(rectangle)
    print("area:", rectangle.area())

    # ==========
    print("=" * 20)

    square = Square(4)
    print(square)
    print("area:", square.area())

    # Çıktı:
    #
    # rectangle 2x3
    # area: 6
    # ====================
    # square 4x4
    # area: 16
