import numpy as np
from matplotlib import pyplot as plt
np.random.seed(1)

#Бернулли
def bernulli(p, n):    
    dsv = np.random.rand(n)
    return np.where(dsv < p, 1, 0)

#Биномиальное
def binomial(m, p, n): 
    return np.array([sum(bernulli(p, m)) for _ in range(n)])

#Геометрическое 
def geometric(p, n):    
    ls = []
    for _ in range(n):
        counter = 0
        while bernulli(p,1)[0] != 1:
            counter += 1
        ls.append(counter+1)
    return np.array(ls)

# Обратное биномиальное
def inverse_binomial(r, p, n):
    ls = []
    for _ in range(n):
        counter = 0
        successes = 0
        while successes < r:
            if bernulli(p,1)[0] == 1:
                successes += 1
            counter += 1
        ls.append(counter)
    return np.array(ls)


def mat(array):
    return np.sum(array)/len(array)

def dispersion(array):
    return mat(array ** 2) - mat(array) ** 2

n = 1000
p = 0.5
bsv = bernulli(p,n)
print('Бернулли')
print(p)
print(mat(bsv))
print(p * (1 - p))
print(dispersion(bsv))

p = 0.2
m = 4
bsv = binomial(m, p, n)
print('Биномиальное')
print(m * p)
print(mat(bsv))
print(m * p * (1 - p))
print(dispersion(bsv))

r = 5
p = 0.25
bsv = inverse_binomial(r, p, n)
print('Обратное биномиальное')
print(r / p)
print(mat(bsv))
print((r * (1 - p)) / p**2)
print(dispersion(bsv))

p = 0.3
bsv = geometric(p,n)
print('Геометрическое')
print(1/p)
print(mat(bsv))
print((1-p)/p**2)
print(dispersion(bsv))