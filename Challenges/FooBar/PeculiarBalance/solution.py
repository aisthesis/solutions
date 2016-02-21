def answer(x):
    digits = _getb3(x)
    answer = []
    i = 0
    while i < len(digits):
        if digits[i] == 0:
            answer.append('-')
        elif digits[i] == 1:
            answer.append('R')
        else:
            answer.append('L')
            _incb3(digits, i)
        i += 1
    return answer

def _getb3(x):
    digits = []
    while x > 0:
        digits.append(x % 3)
        x //= 3
    return digits

def _incb3(digits, ix):
    carry = 1
    for i in range(ix, len(digits)):
        if digits[i] < 2:
            digits[i] += carry
            return
        digits[i] = 0
    digits.append(carry)

