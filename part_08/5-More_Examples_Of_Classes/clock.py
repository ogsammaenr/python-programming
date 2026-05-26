class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def tick(self):
        self.seconds += 1

        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1

        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1

        if self.hours == 24:
            self.hours = 0

    def set(self, hours: int, minutes: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0

    def __str__(self):
        hours = "0" + str(self.hours) if self.hours < 10 else str(self.hours)
        minutes = "0" + str(self.minutes) if self.minutes < 10 else str(self.minutes)
        seconds = "0" + str(self.seconds) if self.seconds < 10 else str(self.seconds)

        return hours + " : " + minutes + " : " + seconds


# Test Alanı
if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)

    # Çıkŧı:
    #
    # 23 : 59 : 55
    # 23 : 59 : 56
    # 23 : 59 : 57
    # 23 : 59 : 58
    # 23 : 59 : 59
    # 00 : 00 : 00
    # 00 : 00 : 01
    # 12 : 05 : 00
