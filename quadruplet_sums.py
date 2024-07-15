numbers = [5, 4, 3, 2, 1, 0]

numbers.sort(reverse=True)

def make_change(coins, target, l):
    if len(l) == 4:
        if target == 0:
            return l
        return None
    candidates = [c for c in coins if c <= target]
    for coin in candidates:
        new_l = make_change(coins, target - coin, l + [coin])
        if new_l is not None:
            return new_l
        
print(make_change([0], 0, []))
print(make_change([1, 0], 1, []))
print(make_change([0, 1], 2, []))
print(make_change(numbers, 11, []))