def dice_sum_prob(target_sum, dice=2, sides=6):
    total = sides ** dice
    favorable = 0
    def dfs(rem, cur):
        nonlocal favorable
        if rem == 0:
            if cur == target_sum: favorable += 1
            return
        for v in range(1, sides+1):
            dfs(rem-1, cur+v)
    dfs(dice, 0)
    return favorable / total

def prob_divisible(max_num, d, exclude=None):
    total = max_num
    cnt = max_num // d
    if exclude:
        lcm = d * exclude // gcd(d, exclude)
        cnt -= max_num // lcm
    return cnt / total
