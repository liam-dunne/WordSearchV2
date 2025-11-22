import math

class WordSearch:
    def __init__(self, grid: str):
        """Initialise grid and size. Raise value error for invalid grids"""
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
    
    def is_present_horizontally(self, word: str) -> bool:
        """Checks each character row by row for a match with given word using two pointers to track position in word and grid.
            Worst case O(n^2) time.
        
            Returns:
                bool: True if word present in grid, False otherwise
            """
        if self.gridSize < len(word):
            return False

        grid = self.grid
        rowLen = self.gridSize
        wordPos = 0 # Pointer to current position in word

        for i in range(len(grid)):
            # Reset wordPos at start of new row
            if i % rowLen == 0:
                wordPos = 0
            # Move to start of next row when no room left in current row for word
            elif (rowLen - (i%rowLen)) < len(word) and wordPos == 0:
                i = (i//rowLen) * (rowLen+1)

            if grid[i] == word[wordPos]:
                wordPos += 1
                if wordPos == len(word):
                    return True
            elif grid[i] == word[0]:
                wordPos = 1

        return False
    