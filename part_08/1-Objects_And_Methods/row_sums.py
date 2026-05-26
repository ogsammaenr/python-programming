def row_sums(matrix: list):
    # satırlardaki elemanlar toplanıp satırın sonuna ekliyoruz
    for row in matrix:
        row.append(sum(row))


# Test alanı
if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)
