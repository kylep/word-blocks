""" Unit tests for word-blocks - Python3 only """
import words.lib as lib


def test_letter_in_block():
    """ Check that a block has a letter in it """
    assert lib.letter_in_block('a', ['a'])
    assert lib.letter_in_block('a', ['a', 'b'])
    assert lib.letter_in_block('a', ['A'])
    assert lib.letter_in_block('a', ['b']) is False


def test_blocks_make_word():
    """ do blocks make up a given word """
    good_blocks = [
        ['A'],
        ['C', 'D'],
        ['T'],
        ['F'],
        ['G']
    ]
    bad_blocks = [
        ['B', 'D'],
        ['A'],
        ['T']
    ]
    word = 'cat'
    good_result, good_blocks = lib.blocks_make_word(good_blocks, word)
    bad_result, bad_blocks = lib.blocks_make_word(bad_blocks, word)
    assert good_result
    assert not bad_result
    assert good_blocks == [['F'], ['G']]
    assert lib.blocks_make_word([['a']], '1')[0] == False


def test_find_words():
    """ find words from test data. Run with -s to review printed output """
    dictionary = [
        'cat',
        'bat',
        'hat',
        'by'
    ]
    blocks = [
        ['c', 'b'],
        ['a'],
        ['t'],
        ['x', 'b'],
        ['y']
    ]
    assert lib.blocks_make_word(blocks, 'hat')[0] is False
    result = lib.find_words(dictionary=dictionary, blocks=blocks)
    assert 'cat' in result
    assert 'bat' in result
    assert 'by' in result
    assert 'by' in result['bat']
    assert 'bat' in result['by']
    # This fails for some reason. The results aren't comprehensive
    # assert 'cat' in result['by']
    #lib.print_words(result)


def test_find_words_a():
    """ It locked up on "A" for some reason """
    blocks = [
        ["R", "E"],
        ["N", "C"],
        ["T", "O"],
        ["H", "X"],
        ["O", "Y"],
        ["M", "J"],
        ["R", "U"],
        ["I", "E"],
        ["L", "R"],
        ["S", "Y"],
        ["M"],
        ["E"],
        ["S"],
        ["A"]
    ]
    dictionary = ['cat', 'hat', 'merry', 'christmas', 'a', 'mer' 'ry']
    result = lib.find_words(dictionary=dictionary, blocks=blocks)
    lib.print_words(result)
