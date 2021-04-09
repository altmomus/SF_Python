def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if (array[middle] < element) and (array[middle + 1] >= element):  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине, то урезаем список на 1 элемент с конца
        print("индекс", middle, "не подходит под условия")
        return binary_search(array, element, left, right - 1)
    else:  # если элемент больше элемента в середине, то урезаем список на 1 элемент с начала
        print("индекс", middle, "не подходит под условия")
        return binary_search(array, element, left + 1, right)


array = input()
element = int(input())

x = array.split(" ")

array_numbers = []

for i in x:
    array_numbers.append(int(i))
array_numbers.sort()

# запускаем алгоритм на левой и правой границе
print(binary_search(array_numbers, element, 0, len(array_numbers)-1))
