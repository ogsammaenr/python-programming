def smallest_average(person1: dict, person2: dict, person3: dict):
    # veriler bir listeye konulur
    person_list = [person1, person2, person3]

    # ortalamalari saklamak icin bir liste oluşturulur
    average_list = [0, 0, 0]

    for i in range(3):
        person = person_list[i]

        # ortalamayı hesaplayip ortalama listesine ekliyoruz
        average_list[i] = (
            person["result1"] + person["result2"] + person["result3"]
        ) / 3

    return person_list[average_list.index(min(average_list))]


# test alanı
if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))

    # Çıktı:
    #
    # {'name': 'Larry', 'result1': 3, 'result2': 1, 'result3': 1}
