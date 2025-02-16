import random
import numpy as np
uniform_random = [random.uniform(0, 1) for _ in range(10)]
print("Distribución Uniforme (random):", uniform_random)
uniform_random_np = np.random.uniform(0, 1, 10)
print("Distribución Uniforme (numpy):", uniform_random_np)
normal_random = [random.gauss(0, 1) for _ in range(10)]
print("Distribución Normal (random):", normal_random)
normal_random_np = np.random.normal(0, 1, 10)
print("Distribución Normal (numpy):", normal_random_np)
binomial_random = np.random.binomial(n=10, p=0.5, size=10)
print("Distribución Binomial:", binomial_random)
poisson_random = np.random.poisson(lam=3.0, size=10)
print("Distribución Poisson:", poisson_random)
exponential_random = np.random.exponential(scale=1.0, size=10)
print("Distribución Exponencial:", exponential_random)
