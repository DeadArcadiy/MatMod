import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve

# Функция, которая использует метод Монте-Карло для решения системы линейных уравнений
def monte_carlo_solve(A, f, num_chains, chain_length):
    n = A.shape[0]  # Размерность системы
    solutions = []  # Список для хранения результатов каждой цепи Маркова
    
    # Симуляция цепей Маркова
    for _ in range(num_chains):
        x = np.zeros(n)  # Начальная точка цепи Маркова
        for _ in range(chain_length):
            # Выбор случайного индекса для обновления
            i = np.random.choice(n)
            # Обновление i-того элемента вектора x
            # Используем формулу: x_i = (f_i - sum(A_ij * x_j for j!=i)) / A_ii
            x[i] = (f[i] - np.dot(A[i, :], x) + A[i, i] * x[i]) / A[i, i]
        solutions.append(x)
    
    # Вычисление среднего решения из всех смоделированных цепей Маркова
    average_solution = np.mean(solutions, axis=0)
    return average_solution, solutions

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
        mc_solution, _ = monte_carlo_solve(A, f, num_chains, chain_length)
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
