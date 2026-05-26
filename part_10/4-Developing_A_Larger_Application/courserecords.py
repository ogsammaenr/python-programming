class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    def name(self) -> str:
        return self.__name

    def grade(self) -> int:
        return self.__grade

    def credits(self) -> int:
        return self.__credits

    def update_grade(self, new_grade: int):
        # not sadece yukseltilebilir
        if new_grade > self.__grade:
            self.__grade = new_grade


class StudyTracker:
    def __init__(self):
        # str -> Course seklinde verileri saklayan dictionary
        self.__courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        # ilk eklemede course nesnesi olusturuyoruz
        if name not in self.__courses:
            self.__courses[name] = Course(name, grade, credits)
        # eger zaten varsa guncelliyoruz
        else:
            self.__courses[name].update_grade(grade)

    def get_course(self, name: str) -> Course | None:
        return self.__courses.get(name, None)

    # getter
    def all_courses(self):
        return list(self.__courses.values())


class StudyTrackerApplication:
    def __init__(self):
        self.__tracker = StudyTracker()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course_ui(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__tracker.add_course(name, grade, credits)

    def get_course_ui(self):
        name = input("course: ")
        course = self.__tracker.get_course(name)
        if course is None:
            print("no entry for this course")
        else:
            print(f"{course.name()} ({course.credits()} cr) grade {course.grade()}")

    def show_statistics(self):
        courses = self.__tracker.all_courses()
        total_courses = len(courses)

        # hic ders yok ise isi burada bitiriyoruz (sifira bolme hatasini engellemek icin)
        if total_courses == 0:
            print("0 completed courses, a total of 0 credits")
            print("mean 0.0")
            print("grade distribution\n5:\n4:\n3:\n2:\n1:")
            return

        total_credits = sum(c.credits() for c in courses)
        total_grades = sum(c.grade() for c in courses)
        mean_grade = total_grades / total_courses

        print(f"{total_courses} completed courses, a total of {total_credits} credits")
        print(f"mean {mean_grade}")
        print("grade distribution")

        for grade in range(5, 0, -1):
            count = sum(1 for c in courses if c.grade() == grade)
            stars = "x" * count
            print(f"{grade}: {stars}")

    def execute(self):
        self.help()
        while True:
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course_ui()
            elif command == "2":
                self.get_course_ui()
            elif command == "3":
                self.show_statistics()
            print("")


# Test Alanı
if __name__ == "__main__":
    application = StudyTrackerApplication()
    application.execute()

    # Çıktı: (Girdiler = ['1', 'ItP', '3', '5', '2', 'ItP', '1', 'ItP', '5', '5', '2', 'ItP', '1', 'ItP', '1', '5', '2', 'ItP', '2', 'Introduction to Java', '1', 'ACiP', '1', '10', '1', 'ItAI', '2', '5', '1', 'Algo101', '4', '1', '1', 'CompModels', '5', '8', '3', '0'])
    #
    # 1 add course
    # 2 get course data
    # 3 statistics
    # 0 exit
    # command: 1
    # course: ItP
    # grade: 3
    # credits: 5
    #
    # command: 2
    # course: ItP
    # ItP (5 cr) grade 3
    #
    # command: 1
    # course: ItP
    # grade: 5
    # credits: 5
    #
    # command: 2
    # course: ItP
    # ItP (5 cr) grade 5
    #
    # command: 1
    # course: ItP
    # grade: 1
    # credits: 5
    #
    # command: 2
    # course: ItP
    # ItP (5 cr) grade 5
    #
    # command: 2
    # course: Introduction to Java
    # no entry for this course
    #
    # command: 1
    # course: ACiP
    # grade: 1
    # credits: 10
    #
    # command: 1
    # course: ItAI
    # grade: 2
    # credits: 5
    #
    # command: 1
    # course: Algo101
    # grade: 4
    # credits: 1
    #
    # command: 1
    # course: CompModels
    # grade: 5
    # credits: 8
    #
    # command: 3
    # 5 completed courses, a total of 29 credits
    # mean 3.4
    # grade distribution
    # 5: xx
    # 4: x
    # 3:
    # 2: x
    # 1: x
    #
    # command: 0
