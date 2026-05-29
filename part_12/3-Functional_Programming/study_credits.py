from functools import reduce


class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"


def sum_of_all_credits(attempts: list):
    return reduce(lambda acc, attempt: acc + attempt.credits, attempts, 0)


def sum_of_passed_credits(attempts: list):
    # once gecilmis olan nesneleri filtreliyoruz
    passed = filter(lambda x: x.grade >= 1, attempts)

    # sonra gecilen derslerin kredilerini topluyoruz
    return reduce(lambda acc, x: acc + x.credits, passed, 0)


def average(attempts: list):
    # once gecilmis dersleri filtreliyoruz
    passed_courses = list(filter(lambda x: x.grade >= 1, attempts))

    # sonra gecilmis derslerin notlarini topluyoruz
    total_grade = reduce(lambda acc, x: acc + x.grade, passed_courses, 0)

    # en son toplam puani gecilmis ders sayisina bolup ortalamayi buluyoruz
    return total_grade / len(passed_courses)


# Test Alanı
if __name__ == "__main__":
    attempt = CourseAttempt("Data Structures and Algorithms", 3, 10)
    print(attempt)
    print(attempt.course_name)
    print(attempt.credits)
    print(attempt.grade)

    print("\n", "=" * 20, " Part 1 ", "=" * 20, "\n")

    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 4, 5)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    credit_sum = sum_of_all_credits([s1, s2, s3])
    print(credit_sum)

    print("\n", "=" * 20, " Part 2 ", "=" * 20, "\n")

    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    credit_sum = sum_of_passed_credits([s1, s2, s3])
    print(credit_sum)

    print("\n", "=" * 20, " Part 3 ", "=" * 20, "\n")

    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)

    # Çıktı:
    #
    # Data Structures and Algorithms (10 cr) grade 3
    # Data Structures and Algorithms
    # 10
    # 3
    #
    # ====================  Part 1  ====================
    #
    # 20
    #
    # ====================  Part 2  ====================
    #
    # 15
    #
    # ====================  Part 3  ====================
    #
    # 4.0
