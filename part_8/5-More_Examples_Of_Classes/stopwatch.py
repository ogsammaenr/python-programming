class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        self.seconds += 1

        # saniye 60 a vardiginda sifirlanip dakikayi arttiriyoruz
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1

        # dakika 60 a vardiginda saati sifirliyoruz
        if self.minutes == 60:
            self.minutes = 0

    def __str__(self):
        minutes = "0" + str(self.minutes) if self.minutes < 10 else str(self.minutes)
        seconds = "0" + str(self.seconds) if self.seconds < 10 else str(self.seconds)

        return minutes + " : " + seconds


# Test Alanı
if __name__ == "__main__":
    watch = Stopwatch()

    # test çıktısını kısaltmak için saati ilerden başlatıyoruz
    watch.minutes = 59
    watch.seconds = 58

    for i in range(5):
        print(watch)
        watch.tick()

    # Çıktı:
    #
    # 59 : 58
    # 59 : 59
    # 00 : 00
    # 00 : 01
    # 00 : 02
