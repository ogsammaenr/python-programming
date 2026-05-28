class ExamResult:
    def __init__(self, name: str, grade1: int, grade2: int, grade3: int):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3


def best_results(results: list):
    # results listesindegi her result icin grade1/2/3 degerlerinin en buyugu ile yeni bir liste olusturuyoruz
    return [max([result.grade1, result.grade2, result.grade3]) for result in results]


# Test Alanı
if __name__ == "__main__":
    result1 = ExamResult("Peter", 5, 3, 4)
    result2 = ExamResult("Pippa", 3, 4, 1)
    result3 = ExamResult("Paul", 2, 1, 3)
    results = [result1, result2, result3]
    print(best_results(results))

    # Çıktı:
    #
    # [5, 4, 3]
