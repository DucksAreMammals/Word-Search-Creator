from cmath import inf
import random
import sys

min = inf


def main():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    try:
        width = int(sys.argv[1])
        height = int(sys.argv[2])
    except IndexError:
        print('Usage: wordsearch.py width height')
        quit()
    except ValueError:
        print('Width and height must be integers')
        quit()

    words = []

    with open("wordsearch.txt", "r") as file:
        for word in file.readlines():
            word = word.strip().upper()

            real_word = ""

            for letter in word:
                if letter in letters:
                    real_word += letter

            words.append(real_word)

    wordsearch = [[None for i in range(width)] for j in range(height)]

    wordsearch = place_word(words, wordsearch)

    print()

    for y, row in enumerate(wordsearch):
        for x, letter in enumerate(row):
            if letter == None:
                wordsearch[y][x] = random.choice(letters)

    if wordsearch != None:
        for line in wordsearch:
            for letter in line:
                if letter == None:
                    print("- ", end="")
                else:
                    print(letter + " ", end="")
            print()
    else:
        print("Cannot fit")

    create_html(wordsearch, words)


def place_word(wordlist, wordsearch):
    global min

    if len(wordlist) < min:
        min = len(wordlist)
        print(min)

    positions = []

    for dir_x in [-1, 0, 1]:
        for dir_y in [-1, 0, 1]:

            if dir_x == 0 and dir_y == 0:
                continue

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
                    positions.append((x, y, dir_x, dir_y))

    random.shuffle(positions)

    for x, y, dir_x, dir_y in positions:
        can_place = True
        for i, letter in enumerate(wordlist[0]):
            if wordsearch[y + i * dir_y][x + i * dir_x] not in [letter, None]:
                can_place = False
                break

        if can_place:
            added_wordsearch = wordsearch
            placed = True

            for i, letter in enumerate(wordlist[0]):
                added_wordsearch[y + i * dir_y][x + i * dir_x] = letter

            if len(wordlist) > 1:
                returned = place_word(wordlist[1:], added_wordsearch)

                if returned != None:
                    return(added_wordsearch)
            else:
                return added_wordsearch

    return None


def create_html(wordsearch, words):
    with open('wordsearch.html', 'w') as file:
        file.write(
            '<!doctype html><html style="font-family:monospace"><head><title>Wordsearch</title></head><body><div style="border:3px solid black;border-radius:10px;margin 1em;padding:.25em .5em;display:inline-block"')

        for row in wordsearch:
            for letter in row:
                file.write(" ")
                file.write(letter)
            file.write('<br>')

        file.write('</div><table style="margin:2em 0;width: 100%">')

        for i, word in enumerate(words):
            if i % 5 == 0:
                file.write('<tr>')

            file.write('<td>')
            file.write(word)
            file.write(' </td>')

            if i % 5 == 4:
                file.write('</tr>')

        file.write("</table></body></html>")


if __name__ == '__main__':
    main()
