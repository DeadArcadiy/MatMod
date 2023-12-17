import numpy as np
import matplotlib.pyplot as plt

def first(num_samples):
    u = np.random.uniform(-1, 1, num_samples)
    x = np.tan(np.pi/2 * u)
    weights = (np.pi/2) * (1/np.cos(np.pi/2 * u))**2
    samples = np.exp(-x**6) * weights
    integral = np.mean(samples)
    integral *= 2
    return integral


def second(num_samples):
    r = np.sqrt(np.random.uniform(0, 1, num_samples))
    theta = np.random.uniform(0, 2*np.pi, num_samples)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    func_values = np.log(1 / np.sqrt(x**2 + y**2))
    integral_estimate = np.mean(func_values) * np.pi
    return integral_estimate


def multi(func,answer):
    res = []
    answers = []
    for i in [100,10000,100000,1000000]:
        res.append(func(i))
        answers.append(answer)
    return res,answers



figure, axis = plt.subplots(2)
real = 1.85544
axis[0].plot(multi(first,real)[1])
axis[0].plot(multi(first,real)[0])
real = 1.5708
axis[1].plot(multi(second,real)[1])
axis[1].plot(multi(second,real)[0])
plt.show()