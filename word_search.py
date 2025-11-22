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
        return (self.check_direction(word, "horizontal") or  self.check_direction(word, "vertical"))
    
    def check_direction(self, word: str, direction: str) -> bool:
        """Checks each character column by column for a match with given word using two pointers to track position in word and grid.
            Worst case O(n^2) time.
        
            Returns:
                bool: True if word present top-to-bottom in grid, False otherwise
            """
        
        if self.gridSize < len(word):
            return False

        grid = self.grid
        size = self.gridSize
        wordPos = 0 # Pointer to current position in word

        # Ensure squares counted in correct order
        if direction == "horizontal":
            rowMult = 1
            colMult = size
        elif direction == "vertical":
            rowMult = size
            colMult = 1

        for i in range(size):
            # Reset wordPos at start of new column
            wordPos = 0
            for j in range(size):
                # Move to start of next column when no room left in current column for word
                if size-j < len(word) and wordPos == 0:
                    break

                if grid[colMult*i + rowMult*j] == word[wordPos]:
                    wordPos += 1
                    if wordPos == len(word):
                        return True
                elif grid[colMult*i + rowMult*j] == word[0]:
                    wordPos = 1

        return False
