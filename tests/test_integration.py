""" Integration tests for word-blocks - Python3 only """
import os

import words.lib as lib


def test_load_blocks():
    """ Load & verify the blocks json file """
    path = 'blocks.json'
    assert os.path.exists(path), 'blocks json file needs to exist'
    blocks = lib.load_blocks(path)
    assert isinstance(blocks, list)
    assert isinstance(blocks[0], list)
    assert isinstance(blocks[0][0], str)
    assert lib.blocks_make_word(blocks, 'a')


def test_load_dictionary():
    """ Load the words text file and confirm it shrinks the set"""
    path = 'words.txt'
    assert os.path.exists(path), 'words file needs to exist'
    blocks = lib.load_blocks('blocks.json')
    words = lib.load_dictionary(path, blocks)
    assert isinstance(words, list)
    # The default word dictionary & blocks have 20202 valid words

