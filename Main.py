from numpy import *
import time
import itertools
import csv
import sympy
from copy import copy

FILENAME1 = "./Output/cone.csv"


def app():
    """Основной код программы.

    Ключевые аргументы:
    start_time -- время выполнения программы.
    cyclic_curve -- количество элементов циклической кривой.
    d -- список элементов от 1 до cyclic_curve+1.
    tmp -- список-копия для преобразований и изменения.
    x - фиксируемое значение из циклической кривой.

    Используемые функции:
    arrayCheck(x, tmp) -- Ищет вектор 'C' и потом выполняется функция проверки неравенства.
                        В функцию передается:
                            x - какое-то фиксируемое значение с кривой,
                            tmp - список элементов без x.

    """
    cyclic_curve = int(input("Введите количество точек: "))
    start_time = time.time()
    d = list(range(1, cyclic_curve + 1))
    tmp = copy(d)
    with open(FILENAME1, 'w', newline="") as file:
        writer = csv.writer(file)
        # output = ["n", "k1", "k2", "k3", "c1", "c2", "c3", "c4", "Cone?"]
        output = ["n", "k1", "k2", "k3", "c1", "c2", "c3", "c4"]
        writer.writerow(output)
        file.close()
    for n in range(0, len(d)):
    # for n in range(0, 1):
        x = tmp[n]
        tmp.remove(x)
        arrayCheck(x, tmp)
        tmp = copy(d)
    print("--- %s seconds ---" % (time.time() - start_time))


def arrayCheck(x, tmp):
    """Функция для поиска вектора 'C = (c1, c2, c3, c4)" и последующая проверка неравества конуса

    Ключевые аргументы:
    arrayList -- список со всеми сочетаниями из tmp по 3.
    vec_c -- искомый вектор 'C'.
    output -- строка, выводимая в файл.

    Используемые функции:
    systemCalc(x, arrayList[j][0], arrayList[j][1], arrayList[j][2]) -- поиск вектора 'C' и запись его в переменную vec_c.
                        В функцию передается:
                            x - фиксированное згначение,
                            array[i][0-2] - значения сочетаний.
    checkCone(vec_c, x, tmp) -- проверка неравенств конуса для найденого вектора 'C'.
                        В функцию передается:
                            vec_c - вектор 'C',
                            x - фиксированное значение,
                            tmp - список чисел от 1 до cyclic_curve+1 без x.
    itertools.combinations(tmp, 3) -- возвращает список всех сочетаний из списка tmp по 3 элемента.
    """
    arrayList = list(itertools.combinations(tmp, 3))
    for j in range(0, len(arrayList)):
        vec_c = systemCalc(x, arrayList[j][0], arrayList[j][1], arrayList[j][2])
        if checkCone(vec_c, x, tmp) == True:
            # output = [x, arrayList[j][0], arrayList[j][1], arrayList[j][2], vec_c[0], vec_c[1], vec_c[2], vec_c[3], "+"]
            output = [x, arrayList[j][0], arrayList[j][1], arrayList[j][2], vec_c[0], vec_c[1], vec_c[2], vec_c[3]]
            with open(FILENAME1, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(output)
        # else:
        #     output = [x, arrayList[j][0], arrayList[j][1], arrayList[j][2], vec_c[0], vec_c[1], vec_c[2], vec_c[3], "-"]
        #     with open(FILENAME1, "a", newline="") as file:
        #         writer = csv.writer(file)
        #         writer.writerow(output)


def systemCalc(n, k1, k2, k3):
    """Поиск вектора 'C' и запись его значений в list_vec_c

    Решение системы линейных уравнений (c,xn)-(c,xk) = 0, где:
                (c,xn) -- скалярное произведение: c1*n + c2*n^2 + c3*n^3 + c4*n^4,
                (c, xk) -- скалярное произведение: c1*k + c2*k^2 + c3*k^3 + c4*k^4.
                Раскрывая скобки (c,xn)-(c,xk)=0 и сокращая на (n-k) мы получаем уравнение:
                    c1 + c2(n+k) + c3(n^2 + n*k + k^2) + c4((n+k)(n^2 + k^2)) = 0.
    Решаем СЛАУ (Ax = b) передав вектор b в функцию LUsolve матрицы A

    Ключевые аргументы:
    a_(1-3) -- (n+k) для k(1-3),
    b_(1-3) -- (n^2 + n*k + k^2) для k(1-3),
    c_(1-3) -- ((n+k)(n^2 + k^2)) для k(1-3),
    matrix1 -- Матрица коэффициентов при c1, c2, c3, c4. Матрица А из (Ax = b),
    v1 -- Вектор значений b из (Ax = b),
    vec_c -- Вектор решений СЛАУ x из (Ax = b),
    c(1-4) -- 4 значения из vec_c,
    list_vec_c -- список со значениями c1, c2, c3, c4.

    Используемые функции:
    vec_c = matrix1.LUsolve(v1) -- решение матричной системы (matrix1 * vec_c = v1) из библиотеки sympy.

    """
    print("")
    print(n, k1, k2, k3)
    a_1 = (n + k1)
    a_2 = (n + k2)
    a_3 = (n + k3)

    b_1 = (pow(n, 2) + (n * k1) + pow(k1, 2))
    b_2 = (pow(n, 2) + (n * k2) + pow(k2, 2))
    b_3 = (pow(n, 2) + (n * k3) + pow(k3, 2))

    c_1 = ((n + k1) * (pow(n, 2) + pow(k1, 2)))
    c_2 = ((n + k2) * (pow(n, 2) + pow(k2, 2)))
    c_3 = ((n + k3) * (pow(n, 2) + pow(k3, 2)))
    # print(1.0, a_1, b_1, c_1)
    # print(1.0, a_2, b_2, c_2)
    # print(1.0, a_3, b_3, c_3)
    matrix1 = sympy.Matrix([[1, a_1, b_1, c_1], [1, a_2, b_2, c_2], [1, a_3, b_3, c_3], [1, 1, 1, 1]])

    v1 = sympy.Matrix(4, 1, [0, 0, 0, 100])
    try:
        vec_c = matrix1.LUsolve(v1)
        c1 = vec_c[0]
        c2 = vec_c[1]
        c3 = vec_c[2]
        c4 = vec_c[3]

        list_vec_c = list([c1, c2, c3, c4])
        # print("1:", (c1 + c2 * a_1 + c3 * b_1 + c4 * c_1))
        # print("2:", (c1 + c2 * a_2 + c3 * b_2 + c4 * c_2))
        # print("3:", (c1 + c2 * a_3 + c3 * b_3 + c4 * c_3))
        # print("4:", (c1+c2+c3+c4))
        return list_vec_c
    except linalg.LinAlgError:
        print("Неподходящие числа")


def checkCone(vec_c, n, k):
    """Проверка всех скалярных произведений конуса для k (от 1 до cyclic_curve без x).

    Просматривает все скалярные произведения вида: c1 + c2(n+k) + c3(n^2 + n*k + k^2) + c4((n+k)(n^2 + k^2)) = 0.
    Возвращает True или False.

    Ключевые аргументы:
    c(1-4) -- значения вектора 'C', передаваемого в эту функцию,
    alpha -- (n+k) из скалярного произведения для фиксированного n и всех k из списка,
    beta -- (n^2 + n*k + k^2) из скалярного произведения для фиксированного n и всех k из списка,
    gamma -- ((n+k)(n^2 + k^2)) из скалярного произведения для фиксированного n и всех k из списка,
    lc -- проверяемое неравенство (c,xn)-(c,xk) >= 0:
                    lc = c1 + c2*alpha + c3*beta + c4*gamma,
                    неравенство проверятся для всех k из передаваемого списка.
    """
    check = True
    c1 = vec_c[0]
    c2 = vec_c[1]
    c3 = vec_c[2]
    c4 = vec_c[3]
    print("c1:", c1, "c2:", c2, "c3:", c3, "c4:", c4)
    for i in range(0, len(k)):
        # alpha = n + k[i]
        # beta = (pow(n, 2)) + (n * k[i]) + (pow(k[i], 2))
        # gamma = (n + k[i]) * (pow(n, 2) + pow(k[i], 2))
        # lc = c1 + (c2 * alpha) + (c3 * beta) + (c4 * gamma)

        # a1 = n - k[i]
        # a2 = pow(n, 2) - pow(k[i], 2)
        # a3 = pow(n, 3) - pow(k[i], 3)
        # a4 = pow(n, 4) - pow(k[i], 4)
        # lc = c1*a1 + c2*a2 + c3*a3 + c4*a4

        lc = c1*pow(n, 1) + c2*pow(n, 2) + c3*pow(n, 3) + c4*pow(n, 4)
        rc = c1*pow(k[i], 1) + c2*pow(k[i], 2) + c3*pow(k[i], 3) + c4*pow(k[i], 4)
        print("k:", k[i], ";", lc, ">=", rc)
        if lc >= rc:

        # lc = c1*(n - k[i]) + c2*(pow(n, 2) - pow(k[i], 2)) + c3*(pow(n, 3) - pow(k[i], 3)) + c4*(pow(n, 4) - pow(k[i], 4))
        # print("k:", k[i], ";", lc, ">=", 0)
        # if lc >= 0:
            check = True
        else:
            return False
    if check:
        return True
    else:
        return False


app()
