
def make_change(coins, target, length):
    if length == 0:
        return [] if target == 0 else None
    candidates = [c for c in coins if c <= target]
    for coin in candidates:
        new_l = make_change(coins, target - coin, length - 1)
        if new_l is not None:
            return [coin] +  new_l
        
print(make_change([0], 0, 4))
print(make_change([1, 0], 1, 4))
print(make_change([0, 1], 2, 4))

numbers = [5, 4, 3, 2, 1, 0]

print(make_change(numbers, 11, 4))