import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve

# Функция, которая использует метод Монте-Карло для решения системы линейных уравнений
def monte_carlo_solve(A, f, num_chains, chain_length):
    A = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]]) - A
    n = A.shape[0]
    x = np.zeros(n)
    for j in range(n):
        for _ in range(num_chains):
            weight = 1
            state_prev = j
            state_new = 0
            x[j] += f[j]
            for _ in range(chain_length):
                state_new = np.random.choice(n)
                weight *= n * A[state_prev][state_new]
                x[j] += weight * f[state_new]
                state_prev = state_new
    return x / num_chains

# Функция для расчета ошибки между решениями метода Монте-Карло и прямого метода
def calculate_error(mc_solution, direct_solution):
    return np.linalg.norm(mc_solution - direct_solution)

A = np.array([[1.2, 0.1, -0.3],
              [-0.3, 0.9, -0.2],
              [0.4, 0.5, 1.0]])
f = np.array([2, 3, 3])
direct_solution = solve(A, f)

num_chains_set = [10, 100, 1000]  # Количество цепей Маркова для симуляции
chain_length_set = [10, 100, 1000]  # Длина цепи Маркова

# Словарь для хранения результатов
results = {}

# Симуляция метода Монте-Карло с различными параметрами и расчет ошибки
for num_chains in num_chains_set:
    for chain_length in chain_length_set:
        mc_solution = monte_carlo_solve(A, f, num_chains, chain_length)
        print('Количество цепей:' + str(num_chains))
        print('Длина цепей:' + str(chain_length))
        print(mc_solution)
        print(direct_solution)
        print('_'*100)
        error = calculate_error(mc_solution, direct_solution)
        results[(num_chains, chain_length)] = error

# Построение графиков
plt.figure(figsize=(14, 7))

for i, num_chains in enumerate(num_chains_set):
    errors = [results[(num_chains, cl)] for cl in chain_length_set]
    plt.plot(chain_length_set, errors, label=f'Num Chains: {num_chains}')

plt.xlabel('Chain Length')
plt.ylabel('Error')
plt.yscale('log')
plt.xscale('log')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()
