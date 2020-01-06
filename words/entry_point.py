""" Handles executing the word-blocks command """
import click

import words.lib


@click.option('--dictionary-path', required=True, help='Text dictionary path')
@click.option('--blocks-path', required=True, help='Blocks json path')
@click.option('--debug-interval', default=0)
@click.command()
def main(dictionary_path, blocks_path, debug_interval):
    """ Run the word-blocks command """
    click.echo(f'loading blocks file {blocks_path}')
    blocks = words.lib.load_blocks(blocks_path)
    click.echo(f'loading dictionary file {dictionary_path}')
    dictionary = words.lib.load_dictionary(dictionary_path, blocks)
    click.echo(f'Building word tree from {len(dictionary)} options')
    words_tree = words.lib.find_words(dictionary, blocks,
                                      progress_interval=debug_interval)
    click.echo('Printing words...')
    words.lib.print_words(words_tree)
