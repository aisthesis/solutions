"""
Copyright (c) 2016 Marshall Farrier

Description
===========
Given an input `n` find the minimal number of squares whose
sum is `n`.

Examples
--------
answer(24) # 3: 16 + 4 + 4
answer(160) # 2: 144 + 16
"""

def answer(n):
    return SquareSolver(n).get_answer()

class SquareSolver(object):

    def __init__(self, n):
        self.n = n
        self.squares = self._get_squares()
        self.memo = [0] * (n + 1)

    def get_answer(self):
        return self._get_ans(self.n)

    def _get_squares(self):
        squares = []
        i = 1
        i_sq = i * i
        while i_sq <= self.n:
            squares.append(i_sq)
            i += 1
            i_sq = i * i
        return squares

    def _get_ans(self, m):
        if self.memo[m]:
            return self.memo[m]
        if m in self.squares:
            self.memo[m] = 1
            return self.memo[m]
        best_ans = m
        for square in self.squares:
            if square > m:
                break
            ans = self._get_ans(m - square) + 1
            if ans < best_ans:
                best_ans = ans
        self.memo[m] = best_ans
        return best_ans

if __name__ == '__main__':
    print(answer(24))
    print(answer(160))
    print(answer(1))
    print(answer(10000))
    # leads to RuntimeError: maximum recursion depth exceeded in cmp
    print(answer(9999))
