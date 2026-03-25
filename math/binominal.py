import math
from functools import lru_cache

@lru_cache(maxsize=None)
def comb(n, k):
    """Биномиальный коэффициент C(n,k). Использует math.comb (Python 3.8+)."""
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)

def binomial_prob(n, k, p):
    """Вероятность ровно k успехов в n испытаниях."""
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

def binomial_at_least(n, k, p):
    """Вероятность не менее k успехов."""
    return sum(binomial_prob(n, i, p) for i in range(k, n+1))

def binomial_at_most(n, k, p):
    """Вероятность не более k успехов."""
    return sum(binomial_prob(n, i, p) for i in range(k+1))

def expected_value_binomial(n, p):
    """Математическое ожидание биномиального распределения."""
    return n * p

def variance_binomial(n, p):
    """Дисперсия биномиального распределения."""
    return n * p * (1 - p)

def sum_of_coefficients(n):
    """Сумма биномиальных коэффициентов Σ C(n,k) = 2^n."""
    return 2 ** n

def sum_of_weighted_coefficients(n):
    """Σ k * C(n,k) = n * 2^(n-1)."""
    return n * (2 ** (n - 1)) if n > 0 else 0

def sum_of_squares_coefficients(n):
    """Σ C(n,k)^2 = C(2n, n)."""
    return comb(2*n, n)
