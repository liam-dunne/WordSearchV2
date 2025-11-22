from word_search import WordSearch
import pytest

validGrids = {"ptjwicbqn" : 3,
         "maudqrkhyectvszl": 4,
         "ylcpfsaungoqwidtkvrbmzjecxhwupsqlong": 6}

invalidGrids = ["", "ascgqw"]
       

def test_get_correct_grid_size():
    for key in validGrids.keys():
        ws = WordSearch(key)
        assert ws.get_grid_size(key) == validGrids[key]

def test_reject_invalid_grids():
    for grid in invalidGrids:
        with pytest.raises(ValueError):
            ws = WordSearch(grid)