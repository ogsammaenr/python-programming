class Task:
    # benzersiz ID leri takip etmek icin sinif degiskeni
    id_counter = 0

    def __init__(self, description: str, programmer: str, workload: int):
        Task.id_counter += 1
        self.id = Task.id_counter
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.__finished = False

    def is_finished(self) -> bool:
        return self.__finished

    def mark_finished(self):
        self.__finished = True

    def __str__(self):
        status = "FINISHED" if self.__finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"


class OrderBook:
    def __init__(self):
        self.__orders = []

    def add_order(self, description: str, programmer: str, workload: int):
        # yeni bir task nesnesi olusturup listeye ekliyoruz
        new_task = Task(description, programmer, workload)
        self.__orders.append(new_task)

    # getter
    def all_orders(self) -> list:
        return self.__orders

    def programmers(self) -> list:
        # self.__orders listesindeki task elemanlarinin programmer verileri ile bir liste olusturuyoruz
        # set() ile tekrarı engelliyoruz
        return [set(task.programmer for task in self.__orders)]

    def mark_finished(self, id: int):
        # teker teker tasklari dolasip idyi ariyoruz
        for task in self.__orders:
            if task.id == id:
                task.mark_finished()
                return
        # bulamazsak hata firlatiyoruz
        raise ValueError(f"No task found with id {id}")

    def finished_orders(self) -> list:
        # self.__orders listesindeki finished olarak isaretlenmis tasklar ile bir liste olusturuyoruz
        return [task for task in self.__orders if task.is_finished()]

    def unfinished_orders(self) -> list:
        # self.__orders listesindeki finished olarak isaretlenmemis tasklar ile bir liste olusturuyoruz
        return [task for task in self.__orders if not task.is_finished()]

    def status_of_programmer(self, programmer: str) -> tuple:
        # yazilimciya ait gorevleri filtreliyoruz
        p_tasks = [task for task in self.__orders if task.programmer == programmer]

        finished = [t for t in p_tasks if t.is_finished()]
        unfinished = [t for t in p_tasks if not t.is_finished()]

        # bitmis isler, bitmemis isler, bitmis islerin yuku, bitmemis islerin yuku
        return (
            len(finished),
            len(unfinished),
            sum(task.workload for task in finished),
            sum(task.workload for task in unfinished),
        )


# Test Alanı
if __name__ == "__main__":
    print("\n", "=" * 20, " Part 1 ", "=" * 20, "\n")

    t1 = Task("program hello world", "Eric", 3)
    print(t1.id, t1.description, t1.programmer, t1.workload)
    print(t1)
    print(t1.is_finished())
    t1.mark_finished()
    print(t1)
    print(t1.is_finished())
    t2 = Task("program webstore", "Adele", 10)
    t3 = Task("program mobile app for workload accounting", "Eric", 25)
    print(t2)
    print(t3)

    print("\n", "=" * 20, " Part 2 ", "=" * 20, "\n")
    # testten once sayaci sifirliyoruz
    Task.id_counter = 0

    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)

    for order in orders.all_orders():
        print(order)

    print()

    for programmer in orders.programmers():
        print(programmer)

    print("\n", "=" * 20, " Part 3 ", "=" * 20, "\n")
    # testten once sayaci sifirliyoruz
    Task.id_counter = 0

    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)

    orders.mark_finished(1)
    orders.mark_finished(2)

    for order in orders.all_orders():
        print(order)

    print("\n", "=" * 20, " Part 4 ", "=" * 20, "\n")
    # testten once sayaci sifirliyoruz
    Task.id_counter = 0

    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)

    # Çıktı:
    #
    # ====================  Part 1  ====================
    #
    # 1 program hello world Eric 3
    # 1: program hello world (3 hours), programmer Eric NOT FINISHED
    # False
    # 1: program hello world (3 hours), programmer Eric FINISHED
    # True
    # 2: program webstore (10 hours), programmer Adele NOT FINISHED
    # 3: program mobile app for workload accounting (25 hours), programmer Eric NOT FINISHED
    #
    # ====================  Part 2  ====================
    #
    # 1: program webstore (10 hours), programmer Adele NOT FINISHED
    # 2: program mobile app for workload accounting (25 hours), programmer Eric NOT FINISHED
    # 3: program app for practising mathematics (100 hours), programmer Adele NOT FINISHED
    #
    # {'Adele', 'Eric'}
    #
    # ====================  Part 3  ====================
    #
    # 1: program webstore (10 hours), programmer Adele FINISHED
    # 2: program mobile app for workload accounting (25 hours), programmer Eric FINISHED
    # 3: program app for practising mathematics (100 hours), programmer Adele NOT FINISHED
    #
    # ====================  Part 4  ====================
    #
    # (2, 1, 35, 100)
