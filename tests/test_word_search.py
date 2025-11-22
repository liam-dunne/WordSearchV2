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
            WordSearch(grid)

def test_word_wrap():
    # The word is present in the string, but wraps around the border, so should return false
    rowWrap = ("cake", 5, "pbldoxfdcakemcntudywjskop")
    ws = WordSearch(rowWrap[2])
    assert ws.is_present_horizontally(rowWrap[0]) == False

def test_horizontal_valid_word():
    validHWordGrids = [("cake", 5, "pbldoxcakemcntudywjskopsd"), # Word at end of row
                       ("cake", 5, "pbldocakexmcntudywjskopsd"), # Word at start of row
                  ("testlongwordtwentych", 25, "bmgayiggyacquxletxevsivirosgwzmyiapexvdizqpcdvvkdsrhvyjtazedcrqpxvracmrjivqnrfbbxfzjommowmygndsvdyppxfotvzrvzdlogxvfdhmtcqbyqynpfjslankitbturkpadqhtdwsmrxbhdgwpbnfguzlcoehpbsujslqunlsthntekdcruwxwvvqxgjugzdecdmflvyfdhdenjcluvocjcdmkoepfzxqfhnhffkwidrczcscarvtmzyumhxgfrsmzwfommdybnnqtyozbtdzmrkvoqahuzleerhvqyycfryvhjlsvfqqzrowwbjwpcjveetazgzonakvvthunupegtqrmazwnmujrivejnzvqlsllsqdwxqekzbhqdjrsrwxuxuckybqqvzdhjzqqsrgfoncweqscmlxwcymgvhugwuzfunpwytcoyrlfscmgwpqwsnedcxfibebqqhnylvlmmfgxzhvdhowurakmqjwhidosgngclmyngvbieaaxpqizlpnxywujsgbumqcimgkslitpgtestlongwordtwentychpoubqywqawqbyutpddcqfopdlicaooeqpcduojdxjvnnhqtkxnxt")
                ]
    for group in validHWordGrids:
        ws = WordSearch(group[2])
        assert ws.is_present(group[0]) == True
