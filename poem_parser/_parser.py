#!/usr/bin/env python

import prosodic
import os
import sys
from .__version__ import __version__


LINE_DELIMITER = '<br/>'
METER = 'default_english'

if 'LOGLEVEL' not in os.environ:
    prosodic.config['print_to_screen'] = 0


class Poem:
    def __init__(self, text, title=''):
        self._title = title
        self._text = prosodic.Text(text)
        self._text.parse(meter=METER)

    def __repr__(self):
        return f"Poem(title='{self.title}')"

    @property
    def title(self):
        return self._title

    @property
    def text(self):
        return self._text

    def print(self):
        for p in self.text.bestParses():
            if p:
                print(p)


def print_help(e=None):
    if e:
        print(f'{type(e).__name__}: {str(e)}', file=sys.stderr)
    print(f'Usage: poem_parser [-f FILENAME|TEXT|-h|-v]',
          file=sys.stderr)


def load(filename):
    poem_title = ''
    poem_text = ''
    with open(filename) as f:
        for line in f:
            if line.startswith('#'):
                poem_title = line.split('#')[1].strip()
            elif not line.startswith('\n'):
                poem_text += line.replace(LINE_DELIMITER, '')

    return Poem(poem_text, poem_title)


def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError('No poem provided.')
        elif len(sys.argv) > 3:
            raise ValueError('Too many arguments.')
        elif len(sys.argv) == 3 and '-f' != sys.argv[1]:
            raise ValueError('Invalid argument specified.')

        if '-h' == sys.argv[1]:
            print_help()
        elif '-v' == sys.argv[1]:
            print(f'poem_parser v{__version__}')
        elif '-f' == sys.argv[1]:
            filename = os.path.abspath(sys.argv[-1])
            poem = load(filename)
            poem.print()
        else:
            text = sys.argv[-1]
            poem = Poem(text)
            poem.print()
    except Exception as e:
        print_help(e)


if __name__ == '__main__':
    main()
