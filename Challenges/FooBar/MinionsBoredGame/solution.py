"""
Copyright (c) 2016 Marshall Farrier
license http://opensource.org/licenses/MIT

Minion's bored game
===================

There you have it. Yet another pointless "bored" game created by the bored minions of Professor Boolean.

The game is a single player game, played on a board with n squares in a horizontal row. The minion places a token on the left-most square and rolls a special three-sided die. 

If the die rolls a "Left", the minion moves the token to a square one space to the left of where it is currently. If there is no square to the left, the game is invalid, 
and you start again.

If the die rolls a "Stay", the token stays where it is. 

If the die rolls a "Right", the minion moves the token to a square, one space to the right of where it is currently. If there is no square to the right, the game is 
invalid and you start again.

The aim is to roll the dice exactly t times, and be at the rightmost square on the last roll. If you land on the rightmost square before t rolls are done then the only valid dice 
roll is to roll a "Stay". If you roll anything else, the game is invalid (i.e., you cannot move left or right from the rightmost square).

To make it more interesting, the minions have leaderboards (one for each n,t pair) where each minion submits the game he just played: the sequence of dice rolls. If some minion has 
already submitted the exact same sequence, they cannot submit a new entry, so the entries in the leader-board correspond to unique games playable. 

Since the minions refresh the leaderboards frequently on their mobile devices, as an infiltrating hacker, you are interested in knowing the maximum possible size a leaderboard can 
have.

Write a function answer(t, n), which given the number of dice rolls t, and the number of squares in the board n, returns the possible number of unique games modulo 123454321. i.e. 
if the total number is S, then return the remainder upon dividing S by 123454321, the remainder should be an integer between 0 and 123454320 (inclusive).

n and t will be positive integers, no more than 1000. n will be at least 2.

Solution
========
Fill in an array representing the number of ways to get to the beginning (makes indexing easier) from square i in t moves.
Let's consider t = 5, n = 4 and derive the answer from the solution for smaller numbers:
For t = 1 there is 1 way to get to the beginning if we are *already at* the beginning, namely *stay*. And there is also
1 way to get to the beginning if we are at n = 2, namely move *left*. So we have for t = 1:
1   1   0   0

Now we consider t = 2. If we are already on square 1, we must stay. 
So far, then, we have:
1   0   0   0
If we are on square *2* with 2 moves, we could consider moving right (0 valid solutions) or staying (1 valid solution above)
or moving left (1 valid solution above). So that gives us 0 + 1 + 1 = 2 solutions from square 2. So far:
1   2   0   0
On square 3 with 2 moves, we can move left (1), stay (0), or right (0), for a total of 1:
1   2   1   0
Array so far:
1   1   0   0
1   2   1   0

Now we consider 3 moves. For square 1 we must stay:
1   0   0   0
From square 2 we can move left (1), stay (2), or move right (1):
1   4   0   0
From square 3 we get 2 + 1 + 0 = 3:
1   4   3   0
From square 4 we get 1 + 0 = 1:
1   1   0   0
1   2   1   0
1   4   3   1

Now for t = 4:
1   8   8   4
For t = 5:
1   17  20  12
Final solution is:
1   1   0   0
1   2   1   0
1   4   3   1
1   8   8   4
1   17  20  12

And that means there are 12 ways to get to the beginning from the end.

To conserve memory, we only need to maintain 2 rows.
"""

MAX_VAL = 123454321

def answer(t, n):
    return Solver(t, n).run()

class Solver(object):

    def __init__(self, t, n):
        self.t = t
        self.n = n

    def run(self):
        if self.t < self.n - 1:
            return 0
        if self.t == self.n - 1:
            return 1
        # array for dynamic programming
        # conserve memory by only maintaining 2 rows
        self.solved_row = [0] * self.n
        self.curr_row = [0] * self.n
        self._solve_rows()
        return self.curr_row[-1] % MAX_VAL

    def _solve_rows(self):
        # solve first row as above
        self.solved_row[:2] = (1, 1,) 
        for i in range(1, self.t):
            self._solve_row()
            self.solved_row[:] = self.curr_row

    def _solve_row(self):
        self.curr_row[:] = self.solved_row
        for j in range(1, self.n - 1):
            self.curr_row[j] += self.solved_row[j - 1]
            self.curr_row[j] += self.solved_row[j + 1]
        self.curr_row[-1] += self.solved_row[-2]

if __name__ == '__main__':
    # test cases
    # answer: 1
    print(answer(1, 2))
    # answer: 3
    print(answer(3, 2))
    # answer: 12
    print(answer(5, 4))
    
