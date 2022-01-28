import random
import sys
from PIL import Image, ImageDraw, ImageFont
import math

min = math.inf
positions = []


def main():
    global positions

    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    try:
        width = int(sys.argv[1])
        height = int(sys.argv[2])
    except IndexError:
        print('Usage: wordsearch.py width height wordsfilename')
        print('Default is 10 10 wordsearch.txt None')
        width = 10
        height = 10
    except ValueError:
        print('Width and height must be integers')
        print('Usage: wordsearch.py width height wordsfilename')
        print('Default is 10 10 wordsearch.txt None')
        width = 10
        height = 10

    try:
        filename = sys.argv[3]
    except IndexError:
        print('Filename defaults to wordsearch.txt')
        print('Usage: wordsearch.py width height wordsfilename')
        print('This defaults to 10 10 wordsearch.txt None')
        filename = 'wordsearch.txt'

    words = []
    unformatted_words = []

    with open(filename, 'r') as file:
        for word in file.readlines():
            word = word.strip().upper()

            if word != '':
                real_word = ''

                for letter in word:
                    if letter in letters:
                        real_word += letter

                unformatted_words.append(word)
                words.append(real_word)

    wordsearch = [[None for i in range(width)] for j in range(height)]

    wordsearch = place_word(words, wordsearch)

    print()

    if wordsearch != None:
        for row in wordsearch:
            positions.append(row.copy())

        for y, row in enumerate(wordsearch):
            for x, letter in enumerate(row):
                if letter == None:
                    wordsearch[y][x] = random.choice(letters)

        print_search(wordsearch)

        create_html(wordsearch, unformatted_words)
        create_image(wordsearch, unformatted_words)
    else:
        print('Cannot fit')


def place_word(wordlist, wordsearch):
    global min

    if len(wordlist) < min:
        min = len(wordlist)
        print(min)

    weak_positions = []
    strong_positions = []

    for dir_x in [-1, 0, 1]:
        for dir_y in [-1, 0, 1]:
            if dir_x != 0 or dir_y != 0:
                min_x = 0
                min_y = 0
                max_x = len(wordsearch[0]) - 1
                max_y = len(wordsearch) - 1

                if dir_x == -1:
                    min_x = len(wordlist[0]) - 1

                if dir_x == 1:
                    max_x = max_x - len(wordlist[0]) + 1

                if dir_y == -1:
                    min_y = len(wordlist[0]) - 1

                if dir_y == 1:
                    max_y = max_y - len(wordlist[0]) + 1

                for x in range(min_x, max_x + 1):
                    for y in range(min_y, max_y + 1):
                        strong = False
                        can_place = True
                        for i, letter in enumerate(wordlist[0]):
                            word_letter = wordsearch[y+i*dir_y][x+i*dir_x]

                            if word_letter == letter:
                                strong = True
                            elif word_letter != None:
                                can_place = False

                        if can_place:
                            if strong:
                                strong_positions.append((x, y, dir_x, dir_y))
                            else:
                                weak_positions.append((x, y, dir_x, dir_y))

    random.shuffle(strong_positions)
    random.shuffle(weak_positions)

    positions = strong_positions + weak_positions

    for x, y, dir_x, dir_y in positions:
        added_wordsearch = []

        for row in wordsearch:
            added_wordsearch.append(row.copy())

        for i, letter in enumerate(wordlist[0]):
            added_wordsearch[y + i * dir_y][x + i * dir_x] = letter

        if len(wordlist) > 1:
            returned = place_word(wordlist[1:], added_wordsearch)

            if returned != None:
                return returned
        else:
            return added_wordsearch

    return None


def create_html(wordsearch, words):
    global positions

    with open('wordsearch.html', 'w') as file:
        file.write(
            '<!doctype html><html><head><title>Wordsearch</title><style>html{font-family:monospace;font-size:2em;white-space:nowrap;text-align:center}div{border:3px solid black;border-radius:10px;margin 1em;padding:.25em .5em;display:inline-block}table{text-align:left;margin:2em 0;width:100%}span{color:blue}td{padding-left:1em}</style></head><body><div>')

        for row in wordsearch:
            for letter in row:
                file.write(' ')
                file.write(letter)
            file.write('<br>')

        file.write('</div><table>')

        for i, word in enumerate(words):
            if i % 3 == 0:
                file.write('<tr>')

            file.write('<td>')
            file.write(word)
            file.write(' </td>')

            if i % 3 == 2:
                file.write('</tr>')

        file.write('</table>')

        # file.write('<div>')

        # for y, row in enumerate(wordsearch):
        #     for x, letter in enumerate(row):
        #         file.write('&nbsp')

        #         if positions[y][x] != None:
        #             file.write('<span>')

        #         file.write(letter)

        #         if positions[y][x] != None:
        #             file.write('</span>')

        #     file.write('<br>')

        # file.write('</div>')

        file.write('</body></html>')


def create_image(wordsearch, words):
    width = len(wordsearch[0]) * 64 + 64
    height = len(wordsearch) * 64 + 64

    max_width = max([len(word) for word in words])
    columns = width // (max_width * 64)

    search_image = Image.new(
        'RGB', (width, height + math.ceil(len(words) / columns) * 76 + 64), (255, 255, 255))
    font = ImageFont.truetype('LiberationMono-Regular.ttf', 64)

    ctx = ImageDraw.Draw(search_image)

    draw_wordsearch(ctx, wordsearch, words, font,
                    width, height, columns, max_width)

    search_image.save('wordsearch.png')


def draw_wordsearch(ctx, wordsearch, words, font, width, height, columns, max_width):
    # Draw box

    margin = 16
    line_width = 8

    start_corner = margin - line_width / 2
    right = width - margin - line_width / 2
    bottom = height - margin - line_width / 2

    shape = (start_corner, start_corner, right, start_corner, right, bottom,
             start_corner, bottom, start_corner, start_corner, start_corner, right)

    ctx.line(shape, (0, 0, 0), line_width, 'curve')

    # Draw letters

    for y, row in enumerate(wordsearch):
        for x, letter in enumerate(row):
            ctx.text((x * 64 + 40, y * 64 + 30), letter, (0, 0, 0), font)

    # Draw words

    start_y = height + 64

    for i in range(columns):
        string = ""

        for word in words[i * math.ceil(len(words) / columns): (i + 1) * math.ceil(len(words) / columns)]:
            string += word
            string += "\n"

        ctx.text((i * max_width * 64 + 64, start_y),
                 string, (0, 0, 0), font, spacing=18)


def print_search(wordsearch):
    for line in wordsearch:
        for letter in line:
            if letter == None:
                print('- ', end='')
            else:
                print(letter + ' ', end='')
        print()


if __name__ == '__main__':
    main()
