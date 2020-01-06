""" Get a non-comprehensive list of words that blocks can make"""
import copy
import json

import click

MIN_WORD_LENGTH = 3
ALLOWED_SHORT_WORDS = ['a', 'i', 'am', 'an', 'be', 'do', 'go', 'he', 'if',
                       'in', 'is', 'it', 'my', 'no', 'oh', 'on', 'or']


def load_blocks(path):
    """ Load the JSON file located at 'path' and return the blocks key """
    with open(path) as json_file:
        data = json.load(json_file)
        return data['blocks']


def letter_in_block(letter, block):
    """ Bool: is a letter in a block """
    for block_letter in block:
        if block_letter.lower() == letter.lower():
            return True
    return False


def blocks_make_word(blocks, word):
    """ Return bool if blocks make word, and the remaining blocks """
    word = word.strip()
    block_cp = copy.deepcopy(blocks)
    for letter in word:
        letter_found = False
        for block in block_cp:
            if letter_in_block(letter, block):
                letter_found = True
                block_cp.remove(block)
                break
        if not letter_found:
            # print(f'letter "{letter}" not in {block_cp} for {word}')
            return False, blocks
    return True, block_cp


def load_dictionary(path, blocks):
    """ Load txt file listing english words, filter to possible from block """
    words = []
    print('LOADING DICTIONARY')
    with open(path) as words_file:
        total = 0
        for word in words_file:
            word = word.strip()
            total += 1
            if len(word) < MIN_WORD_LENGTH and word not in ALLOWED_SHORT_WORDS:
                # The dictionary, and English, has a ton of useless short words
                # like "AA" and "MM"
                continue
            result, rem_blocks = blocks_make_word(blocks, word)
            if result:
                words.append(word)
    print('{}/{} usable words found'.format(len(words), total))
    return words


def find_words(dictionary, blocks, line='', progress_interval=0):
    """ Return a dict tree of words made from the given blocks """
    x = line.replace(" ", "")
    print(f'{line} ({len(x)} blocks)')
    blocks_cp = copy.deepcopy(blocks)
    words = {}
    for entry in dictionary:
        if progress_interval != 0:
            index = dictionary.index(entry)
            if index % progress_interval == 0:
                dictionary_length = len(dictionary)
                print(f'{index} / {dictionary_length} ({entry})')
        made_word, remaining_blocks = blocks_make_word(blocks_cp, entry)
        if made_word:
            words[entry] = find_words(dictionary, remaining_blocks,
                                      line=f'{line} {entry}')
    return words


def print_words(words, line=''):
    """ Accepts a nested word tree dict, prints it """
    for key in words:
        new_line = f'{line} {key}'
        if words[key] == {}:
            click.echo(new_line.lstrip())
        else:
            print_words(words[key], new_line)
