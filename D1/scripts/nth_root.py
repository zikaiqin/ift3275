# Stolen from https://stackoverflow.com/questions/55436001/cube-root-of-a-very-large-number-using-only-math-library

def nth_root(x, n):
    high = 1
    while high ** n <= x:
        high *= 2
    low = high // 2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid ** n < x:
            low = mid
        elif high > mid and mid ** n > x:
            high = mid
        else:
            return mid
    return mid + 1
