# poem_parser
Parse words into stressed and unstressed syllables.

## Installation
To install:
```bash
$ pip install poem_parser
```

## Example usage
To parse a line:
```bash
$ python -m poem_parser "Just give me the likes, dont pass or scroll"
just|GIVE|me.the|LIKES|dont|PASS|or|SCROLL
```

To parse a file:
```bash
$ python -m poem_parser -f poem.txt
RO|ses.are|RED
VIOLETS|||are|BLUE
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
