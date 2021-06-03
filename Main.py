from array import array
from math import fabs, pi
from os import pardir, system, write
from numpy import dot, matmul, piecewise, round, array, linalg
import time
import itertools
import csv
from copy import copy

FILENAME1 = "./Output/cone.csv"
ROUND = 2
def app():
    N = int(input("Введите количество точек: "))
    start_time = time.time()
    d = list(range(1, N+1))
    tmp = copy(d)
    with open(FILENAME1, 'w', newline="") as file:
        writer = csv.writer(file)
        output = ["n","k1","k2","k3","c1","c2","c3","c4", "Cone?"]
        writer.writerow(output)
        file.close()
    # for n in range(0, len(d)):
    for n in range(0, 1):
        x = tmp[n]
        tmp.remove(x)
        arrayCheck(x, tmp)
        x = 0
        tmp = copy(d)
    print("--- %s seconds ---" % (time.time() - start_time))

def arrayCheck(x, tmp):
    array1 = list(itertools.combinations(tmp, 3))
    tmp2 = list(tmp)
    for j in range(0, len(array1)):
        C = systemCalc(x, array1[j][0], array1[j][1], array1[j][2])
        tmp2.remove(array1[j][0])
        tmp2.remove(array1[j][1])
        tmp2.remove(array1[j][2])
        if checkCone(C, x, tmp2) == True:
            output = [x, array1[j][0], array1[j][1], array1[j][2], round(C[0],ROUND), round(C[1],ROUND), round(C[2],ROUND), round(C[3],ROUND), "+"]
            tmp2 = list(tmp)
        else:
            output = [x, array1[j][0], array1[j][1], array1[j][2], round(C[0],ROUND), round(C[1],ROUND), round(C[2],ROUND), round(C[3],ROUND), "-"]
            tmp2 = list(tmp)
        with open(FILENAME1, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(output)

# return C = (c1, c2, c3, c4)
def systemCalc(n, k1, k2, k3):
    #! print(n, k1, k2, k3)
    A1 = float(n + k1)
    A2 = float(n + k2)
    A3 = float(n + k3)
    
    B1 = float(pow(n,2) + n*k1 + pow(k1,2))
    B2 = float(pow(n,2) + n*k2 + pow(k2,2))
    B3 = float(pow(n,2) + n*k3 + pow(k3,2))   

    C1 = float((n+k1) * (pow(n,2) + pow(k1,2)))
    C2 = float((n+k2) * (pow(n,2) + pow(k2,2)))
    C3 = float((n+k3) * (pow(n,2) + pow(k3,2)))
    # print(1.0, A1, B1, C1)
    # print(1.0, A2, B2, C2)
    # print(1.0, A3, B3, C3)
    M1 = array([[1., A1, B1, C1], [1., A2, B2, C2], [1., A3, B3, C3], [1., 1., 1., 1.]])
    # print(M1)
    v1 = array([0.,0.,0.,100.])
    # print(v1)
    try:
        C = linalg.solve(M1, v1)
        #! print (C)
        # for i in range(0, len(C)):
        #     C[i] = round(C[i], ROUND)
        return C
    except linalg.LinAlgError:
        print("Непоходящие числа")

# check (c, xn) >= (c, xk)?   
def checkCone(C, n, k):      
    check = True
    # print(n, C)
    n = float(n + 0.0)
    for i in range(0, len(k)):
        k[i] = float(k[i] + 0.0)
    check = 0
    for i in range(0, len(k)):
        lc = 0   
        # rc = 0 

        # print("i:", i, "k:", k[i])
        # c1 = (round(C[0],ROUND))
        c1 = C[0]
        c2 = C[1]
        c3 = C[2]
        c4 = C[3]
        # c2 = (round(C[1],ROUND))
        # c3 = (round(C[2],ROUND))
        # c4 = (round(C[3],ROUND))

        A1 = float(n + k[i])
        B1 = float(pow(n,2) + n*k[i] + pow(k[i], 2))
        C1 = float(n+k[i])*(pow(n,2) + pow(k[i],2))

        # lc = (c1 + c2*(n+k[i]) + c3*(pow(n,2) + n*k[i] + pow(k[i], 2)) + c4*(n+k[i])*(pow(n,2) + pow(k[i],2)))  
        lc = c1 + c2*A1 + c3*B1 + c4*C1
        
        # lc = c1*n + c2*pow(n,2) + c3*pow(n,3) + c4*pow(n,4)
        # rc = c1*k[i] + c2*pow(k[i], 2) + c3*pow(k[i], 3) + c4*pow(k[i],4)  
        
        # print(round(lc, ROUND), ">=", 0.0) 
        #! print("k:", k[i], ";", lc, ">=", 0.0) 
        # print("k:", k[i], ";", lc, ">=", rc)
        if lc >= 0:
        # if lc >= rc:     
            check = True
        else:
            check = False
            return False           
    if check == True:
        return True
    else: 
        return False

app()