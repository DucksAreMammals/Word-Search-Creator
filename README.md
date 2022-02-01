# Word-Search-Creator

![GitHub last commit](https://img.shields.io/github/last-commit/DucksAreMammals/Word-Search-Creator?style=flat)
![GitHub repo size](https://img.shields.io/github/repo-size/DucksAreMammals/Word-Search-Creator?style=flat)
![Lines of code](https://img.shields.io/tokei/lines/github/DucksAreMammals/Word-Search-Creator?style=flat)

This program makes word searches.

## Dependencies

It only depends on pillow.

## Usage

To use, run ```python wordsearch.py```

By default, the options are set at 25 letters width, 25 letters height, and wordsearch.txt as the input file.

To set options, use ```python wordsearch.py <width> <height> <input filename>```

For example, ```python wordsearch.py 15 20 input.txt``` makes a wordsearch of width 15, a height of 20, and with the words in input.txt.

Input filename, width, height or just the input filename can be excluded.

For example:

Running ```python wordsearch.py``` is the equivalent to running ```python wordsearch.py 25 25 wordsearch.txt```<br>
Running ```python wordsearch.py 10 15``` is the equivalent to running ```python wordsearch.py 10 15 wordsearch.txt```
