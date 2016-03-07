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
        self.prev_memo = [0] * (n + 1)
        self.curr_memo = self.prev_memo[:]
        for square in self.squares:
            self.prev_memo[square] = 1

    def get_answer(self):
        while not self.prev_memo[self.n]:
            self._fill_memo()
        return self.prev_memo[self.n]

    def _get_squares(self):
        squares = []
        i = 1
        i_sq = i * i
        while i_sq <= self.n:
            squares.append(i_sq)
            i += 1
            i_sq = i * i
        return squares

    def _fill_memo(self):
        self.curr_memo = self.prev_memo[:]
        for i in range(1, self.n + 1):
            if self.prev_memo[i]:
                for square in self.squares:
                    if square + i > self.n:
                        break
                    if not self.curr_memo[i + square]:
                        self.curr_memo[i + square] = self.prev_memo[i] + 1
        self.prev_memo = self.curr_memo[:]

if __name__ == '__main__':
    print(answer(24))
    print(answer(160))
    print(answer(1))
    print(answer(10000))
    print(answer(9999))
