from math import factorial
from collections import Counter

def comb(n, k):
    if k < 0 or k > n: return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

def perm_multinomial(word):
    cnt = Counter(word)
    total = factorial(len(word))
    for v in cnt.values():
        total //= factorial(v)
    return total

def stars_and_bars(n, k):
    return comb(n + k - 1, k - 1)

def words_not_starting_with(word, forbidden):
    total = perm_multinomial(word)
    for ch in forbidden:
        if ch in word:
            cnt = Counter(word)
            cnt[ch] -= 1
            sub = factorial(len(word)-1)
            for v in cnt.values():
                sub //= factorial(v)
            total -= sub
    return total
