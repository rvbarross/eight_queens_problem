import random


class EightQueens:
    def __init__(self):
        self.board = []
        self.n_queens = 0
        self.attempts = 0

    def solve(self):
        self.n_queens = 0
        self.attempts = 0
        self.board = []
        while(self.attempts < 7):
            if self.n_queens == 0:
                row = random.randint(0,7)
                self.board.append(row)
                self.n_queens += 1
                print(f'rainha colocada na posição {0} {row}')
            self.set_queen_position(self.n_queens)
            self.attempts += 1
            
        if self.n_queens != 8:
            return False
        elif self.n_queens == 8:
            print('solved')
            return True

    def set_queen_position(self, col):
        n_possibilities = []
        for y in range(col):
            s = set()
            for x in range(8):
                if x > self.board[y]:
                    if x != (self.board[y] + (col-y)):
                        s.add(x)
                elif x < self.board[y]:
                    if x != (self.board[y] - (col-y)):
                        s.add(x)
            n_possibilities.append(s)
        
        if len(n_possibilities) != 0:
            n_t_possibilities = list(n_possibilities[0])
            if len(n_t_possibilities) > 1:
                for x in range(len(n_possibilities) - 1):
                    n_t_possibilities = list(set(n_t_possibilities) & n_possibilities[x+1])


            if len(n_t_possibilities) > 0:
                row = n_t_possibilities[random.randint(0, len(n_t_possibilities) - 1)] 
                self.board.append(row)
                self.n_queens += 1
                print(f'rainha colocada na posição {col} {row}')
    


if __name__ == '__main__':
    e = EightQueens()
    while True:
        is_resolved = e.solve()
        if is_resolved:
            break
