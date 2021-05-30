from array import array
from math import fabs
from os import system, write
import numpy
import sys
import itertools
import csv
import copy
FILENAME = "cone.csv"

def main():
    N = int(input("Введите количество точек: "))
    d = list(range(1, N+1))
    tmp = copy.copy(d)
    with open(FILENAME, 'w', newline="") as file:
        writer = csv.writer(file)
        output = ["n","k1","k2","k3","C1","C2","C3","C4", "Cone?"]
        writer.writerow(output)
        file.close()
    for n in range(0, len(d)):
        x = d[n]
        tmp.pop(n)
        arr(x, tmp)
        tmp = copy.copy(d)
    

def arr(x, tmp):
    array1 = list(itertools.combinations(tmp, 3))
    for j in range(0, len(array1)):
        C = systemCalc(x, array1[j][0], array1[j][1], array1[j][2])
        if secCone(C, x, tmp) == True:
            output = [x, array1[j][0], array1[j][1], array1[j][2], round(C[0],2), round(C[1],2), round(C[2],2), round(C[3],2), "+"]
        else:
            output = [x, array1[j][0], array1[j][1], array1[j][2], round(C[0],2), round(C[1],2), round(C[2],2), round(C[3],2), "-"]
        with open(FILENAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(output)
        
    print("\n")

# def mainCone(C, n, k1, k2, k3, check):
#     if (C[0]*n + C[1]*n + C[2]*n + C[3]*n == C[0]*k1 + C[1]*k1 + C[2]*k1 + C[3]*k1):
#         if (C[0]*n + C[1]*n + C[2]*n + C[3]*n == C[0]*k2 + C[1]*k2 + C[2]*k2 + C[3]*k2):
#             if (C[0]*n + C[1]*n + C[2]*n + C[3]*n == C[0]*k3 + C[1]*k3 + C[2]*k3 + C[3]*k3):
#                 return check+3
#             else:
#                 return check+0
#         else:
#             return check+0
#     else:
#         return check+0

def secCone(C, n, k):   
    check = 0
    for i in range(0, len(k)):
        check = C[0]*n + C[1]*pow(n,2) + C[2]*pow(n,3) + C[3]*pow(n,4) >= C[0]*k[i] + C[1]*pow(k[i],2) + C[2]*pow(k[i],3) + C[3]*pow(k[i],4)
        if check == False:
            return 0
    if check == True:
        return True
    else: 
        return False

def systemCalc(n, k1, k2, k3):
    
    A1 = n + k1
    A2 = n + k2
    A3 = n + k3
    # print("A1:" + str(A1))
    # print("A2:" + str(A2))
    # print("A3:" + str(A3), end="\n\n")

    B1 = (pow(n,2) + n*k1 + pow(k1,2))
    B2 = (pow(n,2) + n*k2 + pow(k2,2))
    B3 = (pow(n,2) + n*k3 + pow(k3,2))
    # print("B1:" + str(B1))
    # print("B2:" + str(B2))
    # print("B3:" + str(B3), end="\n\n")

    C1 = (n+k1) * ((n*n) + (k1*k1))
    C2 = (n+k2) * ((n*n) + (k2*k2))
    C3 = (n+k3) * ((n*n) + (k3*k3))
    # print("C1:" + str(C1))
    # print("C2:" + str(C2))
    # print("C3:" + str(C3), end="\n\n")

    M1 = numpy.array([[1., A1, B1, C1], [1., A2, B2, C2], [1., A3, B3, C3], [1., 1., 1., 1.]])
    v1 = numpy.array([0.,0.,0.,100.])
    try: 
        C = numpy.linalg.solve(M1, v1)
        print("n = " + str(n), "k1 = " + str(k1), "k2 = " + str(k2), "k3 = " + str(k3), "C1 = ", str(C[0]), "C2 = ", str(C[1]), "C3 = ", str(C[2]), "C4 = ", str(C[3]))
        return C       
        
    except numpy.linalg.LinAlgError:
        print("Непоходящие числа")
    
    
main()