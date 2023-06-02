def insert_at_beginning(element, target_list):
    b = []
    if len(target_list) == 0:
        target_list.append(element)
    else:
        b.append(element)
        for index in range(1, len(target_list) + 1):
            b.append(0)
        for index in range(0, len(target_list)):
            b[index + 1] = target_list[index]
    return b


def sum_of_lists(target_list):
     sum = 0
     for num in range(len(target_list)):
        for nums in range(len(target_list[num])):
            sum += target_list[num][nums]
        return sum

def sum_of_diagonals(target_list):
    sum = 0
    for row in range(len(target_list)):
        for col in range(len(target_list[row])):
            if row == col or row == row + col - 1:
                sum += target_list[row][col]
    return sum


def transpose_array(target_list):
    for i in range(len(target_list)):
        for j in range(len(target_list[i])):
            print(target_list[j][i], end=" ")
    print()


def sum_of_two_arrays(list_one, list_two):
    c = []
    for i in range(len(list_one)):
        for j in range(len(list_one[i])):
            c.append(list_one[i][j] + list_two[i][j])
    return c


def matrix_multiplication(list_one, list_two):
    for i in range(len(list_one)):
        for j in range(len(list_one[i])):
            sum = 0
            for k in range(len(list_two[i])):
                sum += list_one[i][k] * list_two[k][j]
            print(sum, end=" ")
        print()


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(insert_at_beginning(10, a))
print(sum_of_lists(a))
print(sum_of_diagonals(a))
transpose_array(a)
print(sum_of_two_arrays(a, b))
matrix_multiplication(a, b)
    