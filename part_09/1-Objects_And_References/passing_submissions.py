class ExamSubmission:
    def __init__(self, examinee: str, points: int):
        self.examinee = examinee
        self.points = points

    # sorudaki cikti formatini elde edebilmek icin eklendi
    def __str__(self):
        return f"ExamSubmission (examinee: {self.examinee}, points: {self.points})"


def passed(submissions: list, lowest_passing: int):
    # sart saglanan nesneler ile yeni bir liste olusturularak donduruldu
    return [sub for sub in submissions if sub.points >= lowest_passing]


# Test Alanı
if __name__ == "__main__":
    s1 = ExamSubmission("Peter", 12)
    s2 = ExamSubmission("Pippa", 19)
    s3 = ExamSubmission("Paul", 15)
    s4 = ExamSubmission("Phoebe", 9)
    s5 = ExamSubmission("Persephone", 17)

    passes = passed([s1, s2, s3, s4, s5], 15)
    for passing in passes:
        print(passing)
