# Google online challenge
# Get the sum of the digits iteratively
# until the sum is a single digit

def answer(x):
    if x < 10:
        return x
    total = 0
    while x > 0:
        total += x % 10
        x //= 10
    return answer(total)
