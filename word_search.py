import math

class WordSearch:
    def __init__(self, grid: str):
        gridSize = self.get_grid_size(grid)
        if gridSize == -1:
            raise ValueError("Invalid grid shape")
        
        self.gridSize = gridSize
        self.grid = grid

    def get_grid_size(self, grid: str):
        """Get size of square grid, returning -1 if grid invalid"""
        numSquares = len(grid)
        if numSquares == 0:
            return -1
        
        squareSize = math.sqrt(numSquares)
        if (squareSize.is_integer()): 
            return int(squareSize)
        else:
            return -1

    def is_present(self, word: str) -> bool:
        return True