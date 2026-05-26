class WeatherStation:
    def __init__(self, name: str):
        self.__name = name
        self.__observation = []

    def add_observation(self, observation: str):
        self.__observation.append(observation)

    def latest_observation(self) -> str:
        # eğer listeye hiçbir veri eklenmediyse boş string döndürüyoruz
        if len(self.__observation) == 0:
            return ""

        return self.__observation[-1]

    def number_of_observations(self) -> int:
        return len(self.__observation)

    def __str__(self) -> str:
        # soruda istenen çıktı formatı
        return f"{self.__name}, {self.number_of_observations()} observations"


if __name__ == "__main__":
    station = WeatherStation("Houston")
    print(station.latest_observation())
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)

    # Çıkŧı:
    #
    #
    # Sunny
    # Thunderstorm
    # 3
    # Houston, 3 observations
