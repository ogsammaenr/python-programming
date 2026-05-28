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
        # KONTROL EDEBİLMEK İÇİN EKLENDİ
        if programmer not in [task.programmer for task in self.__orders]:
            return (-1, -1, -1, -1)

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


def main():
    orders = OrderBook()

    print("commands:")
    print("0 exit")
    print("1 add order")
    print("2 list finished tasks")
    print("3 list unfinished tasks")
    print("4 mark task as finished")
    print("5 programmers")
    print("6 status of programmer")
    print()

    while True:
        try:
            print(" ")
            cmd = input("command: ")

            match cmd:
                case "0":
                    break

                case "1":
                    # girdiler
                    desc = input("description: ")
                    prog_work = input("programmer and workload estimate: ")
                    parts = prog_work.split()

                    # girdilerin dogrulugunu kontrol ediyoruz
                    if len(parts) != 2 or not parts[1].isdigit():
                        print("erroneous input")
                        continue

                    orders.add_order(desc, parts[0], int(parts[1]))
                    print("added!")

                case "2":
                    finished = orders.finished_orders()
                    if not finished:
                        print("no finished tasks")
                    else:
                        for task in finished:
                            print(task)

                case "3":
                    unfinished = orders.unfinished_orders()
                    if not unfinished:
                        print("no unfinished tasks")
                    else:
                        for task in unfinished:
                            print(task)

                case "4":
                    # girdi
                    id_str = input("id: ")
                    if not id_str.isdigit():
                        print("erroneous input")
                        continue

                    orders.mark_finished(int(id_str))
                    print("marked as finished")

                case "5":
                    for programmer in orders.programmers():
                        print(programmer)

                case "6":
                    prog_name = input("programmer: ")
                    status = orders.status_of_programmer(prog_name)
                    if status == (-1, -1, -1, -1):
                        print("erroneous input")
                        continue
                    print(
                        f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}"
                    )

                case _:
                    print("erroneous input")

        except ValueError:
            print("erroneous input")


if __name__ == "__main__":
    main()

    # Çıktı: (girdiler = ['1', 'desc1', 'jonah 100', '1', 'desc2', 'eric 25', '1', 'desc3', 'nina 12', '1', 'desc4', 'jonah 55',
    #                   '2', '3', '4', '2', '4', '4', '2', '3', '5', '6', 'jonah', '1', 'descx', 'eric xxx', '1', 'descx', 'eric',
    #                   '4', '1000000', '4', 'xxxx', '6', 'unknownprogrammer'])
    #
    # commands:
    # 0 exit
    # 1 add order
    # 2 list finished tasks
    # 3 list unfinished tasks
    # 4 mark task as finished
    # 5 programmers
    # 6 status of programmer
    #
    #
    # command: 1
    # description: desc1
    # programmer and workload estimate: jonah 100
    # added!
    #
    # command: 1
    # description: desc2
    # programmer and workload estimate: eric 25
    # added!
    #
    # command: 1
    # description: desc3
    # programmer and workload estimate: nina 12
    # added!
    #
    # command: 1
    # description: desc4
    # programmer and workload estimate: jonah 55
    # added!
    #
    # command: 2
    # no finished tasks
    #
    # command: 3
    # 1: desc1 (100 hours), programmer jonah NOT FINISHED
    # 2: desc2 (25 hours), programmer eric NOT FINISHED
    # 3: desc3 (12 hours), programmer nina NOT FINISHED
    # 4: desc4 (55 hours), programmer jonah NOT FINISHED
    #
    # command: 4
    # id: 2
    # marked as finished
    #
    # command: 4
    # id: 4
    # marked as finished
    #
    # command: 2
    # 2: desc2 (25 hours), programmer eric FINISHED
    # 4: desc4 (55 hours), programmer jonah FINISHED
    #
    # command: 3
    # 1: desc1 (100 hours), programmer jonah NOT FINISHED
    # 3: desc3 (12 hours), programmer nina NOT FINISHED
    #
    # command: 5
    # {'nina', 'eric', 'jonah'}
    #
    # command: 6
    # programmer: jonah
    # tasks: finished 1 not finished 1, hours: done 55 scheduled 100
    #
    # command: 1
    # description: descx
    # programmer and workload estimate: eric xxx
    # erroneous input
    #
    # command: 1
    # description: descx
    # programmer and workload estimate: eric
    # erroneous input
    #
    # command: 4
    # id: 1000000
    # erroneous input
    #
    # command: 4
    # id: xxxx
    # erroneous input
    #
    # command: 6
    # programmer: unknownprogrammer
    # erroneous input
    #
    # command: 0
