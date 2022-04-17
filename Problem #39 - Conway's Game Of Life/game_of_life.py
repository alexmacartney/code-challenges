class GameOfLife:
    def __init__(self, n, cells=set()):
        # Each cell will be a tuple (row, col)
        self.cells = cells
        for _ in range(n):
            self.print_board()
            self.next()

    def get_number_of_live_neighbours(self, row, col):
        count = 0
        for cell_row, cell_col in self.cells:
            if abs(cell_row - row) > 1:
                continue
            if abs(cell_col - col) > 1:
                continue
            if cell_row == row and cell_col == col:
                continue
            count += 1
        return count

    def get_neighbouring_cells(self, row, col):
        return set([
            (row - 1, col - 1),
            (row, col - 1),
            (row + 1, col - 1),
            (row - 1, col),
            (row + 1, col),
            (row - 1, col + 1),
            (row, col + 1),
            (row + 1, col + 1),
        ])

    def next(self):
        new_cells = set()
        # Go through each cell, look for neighbours, decide whether to append to new list
        for row, col in self.cells:
            num_of_neighbours = self.get_number_of_live_neighbours(row, col)
            if 2 <= num_of_neighbours <= 3:
                new_cells.add((row, col))

        potential_live_cells = set()
        for row, col in self.cells:
            potential_live_cells = potential_live_cells.union(self.get_neighbouring_cells(row, col))
        potential_live_cells = potential_live_cells - self.cells

        # Go through each potential live cell, get the number of neighbours, and add if = 3
        for row, col in potential_live_cells:
            num_of_neighbours = self.get_number_of_live_neighbours(row, col)
            if num_of_neighbours == 3:
                new_cells.add((row, col))

        self.cells = new_cells

    def get_boundaries(self):
        bottom = min(self.cells, key=lambda cell: cell[0])[0]
        left = min(self.cells, key=lambda cell: cell[1])[1]
        top = max(self.cells, key=lambda cell: cell[0])[0]
        right = max(self.cells, key=lambda cell: cell[1])[1]
        return top, left, bottom, right

    def print_board(self):
        bottom, left, top, right = self.get_boundaries()
        print('--------------------------------------')
        for i in range(bottom, top + 1):
            for j in range(left, right + 1):
                if (i, j) in self.cells:
                    print('*', end='')
                else:
                    print('.', end='')
            print('')
        print('--------------------------------------')