import numpy as np ###Библиотека питона работающая с матрицами  :) https://numpy.org/



operation = int(input("Определить расстояние между вершинами - 1, Определить кол-во маршрутов между вершинами - 2 "))
arrayGraf = [[0,1,1,0,0,0,0],[1,0,0,1,1,0,1],[1,0,0,0,0,1,0],[0,1,0,0,1,0,1],[0,1,0,1,0,0,1],[0,0,1,0,0,0,1],[0,1,0,1,1,1,0]]

# for i in range(7):    ### Заполнение матрицы смежности
#     arrayGraf.append([])
#     for k in range(7):
#         m = int(input("Введите {}-{} элемент матрицы смежности ".format(i + 1, k + 1)))
#         arrayGraf[i].append(m)
# for i in range(len(arrayGraf)):
#     print(arrayGraf[i])


first = int(input("Введите номер первой вершины "))
second = int(input("Введите номер второй вершины "))
mass = np.array(arrayGraf) ### Преобразование матрицы  библиотекой питона в нужный ей формат

def main(first, second, operation, mass): ### Менюшка
    if operation == 1:
        SearchLen(mass, first, second)
    if operation == 2:
        length = int(input("Введите расстояние "))
        CountOfWay(mass, first, second, length)

def SearchLen(mass, first, second, count=1, newMatrix=[]): ###Поиск расстояния между вершинами
    newMatrix = mass
    while newMatrix[first - 1][second - 1] == 0:
        newMatrix = newMatrix.dot(mass)
        count += 1
    print("Расстояние между вершинами {} и {} равно {}".format(first, second, newMatrix[first - 1][second - 1]))
    print("Матрица {} степени:".format(count))
    print(newMatrix)
    return 0


def CountOfWay(mass, first, second, length): ### Определение кол-ва путей заданной длины
    newMatrix = mass
    for i in range(length - 1):
        newMatrix = newMatrix.dot(mass)
    print("Количество маршрутов длинной {} между вершинами {} и {} равно {}".format(length, first, second,
                                                                                    newMatrix[first - 1][second - 1]))
    print("Матрица {} степени".format(length))
    print(newMatrix)
    return 0

main(first, second, operation, mass)

