import random


def main():
    width = int(input("Please enter the width of the wordsearch: "))
    height = int(input("Please enter the height of the wordsearch: "))

    words = []

    with open("wordsearch.txt", "r") as file:
        for word in file.readlines():
            words.append(word.strip().lower())

    wordsearch = [[None for i in range(width)] for j in range(height)]

    wordsearch = place_word(words, wordsearch)

    print()

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


def place_word(wordlist, wordsearch):
    print(str(len(wordlist)))

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


if __name__ == '__main__':
    main()
