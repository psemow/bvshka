def gcd(a, b):
    while b: a, b = b, a % b
    return a

def last_digit_power(base, exp):
    if exp == 0: return 1
    cycle = {0:[0],1:[1],2:[2,4,8,6],3:[3,9,7,1],4:[4,6],
             5:[5],6:[6],7:[7,9,3,1],8:[8,4,2,6],9:[9,1]}
    cyc = cycle[base % 10]
    return cyc[(exp - 1) % len(cyc)]

def sum_of_squares(n):
    return n*(n+1)*(2*n+1)//6
