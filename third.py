import numpy as np
import random
import math
random.seed(1)
np.random.seed(1)


def normal_dist(m, s2, N, n):
    arr = []
    for _ in range(n):
        x = 0
        for _ in range(N):
            x += random.random()
        x -= N/2
        x = m + np.sqrt(12 * s2 / N) * x
        arr.append(x)
    return np.array(arr)

def lognormal_dist(m, s2, N, n):
    arr = normal_dist(m, s2, N, n)
    arr = np.exp(arr)
    return arr

def Koshi(a,b,n):
    arr = np.random.rand(n)
    return a + b * np.tan(np.pi * (arr - 0.5))

def exponential(a,n):
    arr = np.random.rand(n)
    return -1/a * np.log(arr)

def weibull(a, b, n):
    arr = np.random.rand(n)
    return b * (-np.log(1 - arr)) ** (1 / a)

def mat(array):
    return np.sum(array)/len(array)

def dispersion(array):
    return 1/(n-1) * sum(np.power(array - mat(array),2))

def median(array,n):
    a = sorted(array)
    return (a[int(n/2-1)] + a[int(n/2)])/2

####################################
print('Нормальное распределение')
N = 120
n = 100000
m = 4
s2 = 25
arr = normal_dist(m,s2,N,n)
print("Истинное мат ожидание")
print(m)
print("Полученное мат ожидание")
print(mat(arr))
print("Истинная дисперсия")
print(s2)
print("Полученная дисперсия")
print(dispersion(arr))
####################################
print("Коши")
a = 1
b = 2
arr = Koshi(a,b,n)
print("Истинная медиана")
print(a)
print("Полученная медиана")
print(median(arr,n))
####################################
print("Логнормальное распределение")
m = 0
s2 = 4 
arr = lognormal_dist(m,s2,N,n)
print("Истинное мат ожидание")
print(math.exp(m + s2 / 2))
print("Полученное мат ожидание")
print(mat(arr))
print("Истинная дисперсия")
print((math.exp(s2) - 1) * math.exp(2 * m + s2))
print("Полученная дисперсия")
print(dispersion(arr))
####################################
print("Экспоненциальное распределение")
a = 0.5
arr = exponential(a,n)
print("Истинное мат ожидание")
print(1/a)
print("Полученное мат ожидание")
print(mat(arr))
print("Истинная дисперсия")
print(1/a**2)
print("Полученная дисперсия")
print(dispersion(arr))
####################################
print("Распределение Вейбулла")
a = 4
b = 0.5
arr = weibull(a,b,n)
print("Истинное мат ожидание")
print(b * math.gamma(1 + 1/a))
print("Полученное мат ожидание")
print(mat(arr))
print("Истинная дисперсия")
print((b**2) * (math.gamma(1 + 2/a) - (math.gamma(1 + 1/a))**2))
print("Полученная дисперсия")
print(dispersion(arr))