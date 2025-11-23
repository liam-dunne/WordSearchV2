from word_search import WordSearch
import pytest
import random

validChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


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
    colWrap = ("bowl", 5, "dblicuqwoxsbbaslodgadwjfg")
    ws = WordSearch(rowWrap[2])
    assert ws.is_present(rowWrap[0]) == False
    ws = WordSearch(colWrap[2])
    assert ws.is_present(colWrap[0]) == False

def test_horizontal_valid_word():
    validHWordGrids = [("cake", 5, "pbldoxcakemcntudywjskopsd"), # Word at end of row
                       ("cake", 5, "pbldocakexmcntudywjskopsd"), # Word at start of row
                  ("testlongwordtwentych", 25, "bmgayiggyacquxletxevsivirosgwzmyiapexvdizqpcdvvkdsrhvyjtazedcrqpxvracmrjivqnrfbbxfzjommowmygndsvdyppxfotvzrvzdlogxvfdhmtcqbyqynpfjslankitbturkpadqhtdwsmrxbhdgwpbnfguzlcoehpbsujslqunlsthntekdcruwxwvvqxgjugzdecdmflvyfdhdenjcluvocjcdmkoepfzxqfhnhffkwidrczcscarvtmzyumhxgfrsmzwfommdybnnqtyozbtdzmrkvoqahuzleerhvqyycfryvhjlsvfqqzrowwbjwpcjveetazgzonakvvthunupegtqrmazwnmujrivejnzvqlsllsqdwxqekzbhqdjrsrwxuxuckybqqvzdhjzqqsrgfoncweqscmlxwcymgvhugwuzfunpwytcoyrlfscmgwpqwsnedcxfibebqqhnylvlmmfgxzhvdhowurakmqjwhidosgngclmyngvbieaaxpqizlpnxywujsgbumqcimgkslitpgtestlongwordtwentychpoubqywqawqbyutpddcqfopdlicaooeqpcduojdxjvnnhqtkxnxt")
                ]
    for group in validHWordGrids:
        ws = WordSearch(group[2])
        assert ws.is_present(group[0]) == True

def test_vertical_valid_word():
    validVWordGrids = [("light", 8, "nailndubuitiyiusgiugdbnfkzbhmvjqsrgtofhsdhfohsadlkfbklabsdkbnxic")]
    for group in validVWordGrids:
        ws = WordSearch(group[2])
        assert ws.is_present(group[0]) == True

def test_horizontal_invalid_words():
    invalidHWordGrids = [("test", 5, "asdlcnaidsfrheqytsetfdbcv"), # Word appears right-to-left
                         ("might", 7, "lufdhfhdshakluygdcgadsyufkgaselgbfdaqdschsildchsv") # Word doesn't appear at all
                      ]
    for group in invalidHWordGrids:
        ws = WordSearch(group[2])
        assert ws.is_present(group[0]) == False

def test_vertical_invalid_word():
    invalidVWordGrids = [("pink", 6, "kthuiynawlseihdafhpdcllbasdhffhalisd"), # Word appears bottom-to-top
                         ("sight", 7, "lufdhfhdshakluygdcgadsyufkgaselgbfdaqdschsildchsv") # Word doesn't appear at all
                        ]
    for group in invalidVWordGrids:
        ws = WordSearch(group[2])
        assert ws.is_present(group[0]) == False

def test_word_too_big():
    tooBigWords = [("abcdefghijklmnop", 5, "albmcxaijnxuichdzudsfamnn")]
    for group in tooBigWords:
        ws = WordSearch(group[2])
        assert ws.is_present(group[0]) == False

def test_large_grid():
    word = "abcdefgh"
    grid = ""
    for i in range(10000):
        grid += random.choice(validChars)
    grid = grid[:-len(word)] + word 
    
    ws = WordSearch(grid)
    for i in range(100):
        assert ws.is_present(word) == True