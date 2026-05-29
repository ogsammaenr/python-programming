class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return (
            f"{self.student_name}, grade for the course {self.course_name} {self.grade}"
        )


def names_of_students(attempts: list):
    # ogrenci isimlerini map ile aliyoruz list ile liste olusturuyoruz
    return list(map(lambda attempt: attempt.student_name, attempts))


def course_names(attempts: list):
    # ders isimlerini map ile aliyoruz set ile tekrari engelliyoruz sorted ile siraliyoruz
    return sorted(set(map(lambda attempt: attempt.course_name, attempts)))


# Test Alanı
if __name__ == "__main__":
    attempt = CourseAttempt("Peter Python", "Introduction to Programming", 5)
    print(attempt.student_name)
    print(attempt.course_name)
    print(attempt.grade)
    print(attempt)

    print("\n", "=" * 20, " Part 1 ", "=" * 20, "\n")

    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

    for name in names_of_students([s1, s2, s3]):
        print(name)

    print("\n", "=" * 20, " Part 2 ", "=" * 20, "\n")

    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

    for name in course_names([s1, s2, s3]):
        print(name)

    # Çıktı:
    #
    # Peter Python
    # Introduction to Programming
    # 5
    # Peter Python, grade for the course Introduction to Programming 5
    #
    # ====================  Part 1  ====================
    #
    # Peter Python
    # Olivia C. Objective
    # Peter Python
    #
    # ====================  Part 2  ====================
    #
    # Advanced Course in Programming
    # Introduction to Programming
