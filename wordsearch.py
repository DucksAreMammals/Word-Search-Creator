import random


def main():
    width = int(input("Please enter the width of the wordsearch: "))
    height = int(input("Please enter the height of the wordsearch: "))

    words = []

    with open("wordsearch.txt", "r") as file:
        for word in file.readlines():
            words.append(word.strip())

    wordsearch = [[None for i in range(width)] for j in range(height)]

    for word in words:
        placed = False

        while not placed:
            dir_x = random.randint(-1, 1)
            dir_y = random.randint(-1, 1)

            if dir_x == 0 and dir_y == 0:
                if random.random() > 0.5:
                    dir_x = random.choice([1, -1])
                else:
                    dir_y = random.choice([1, -1])

            min_x = 0
            min_y = 0
            max_x = width - 1
            max_y = height - 1

            if dir_x == -1:
                min_x = len(word) - 1

            if dir_x == 1:
                max_x = max_x - len(word) + 1

            if dir_y == -1:
                min_y = len(word) - 1

            if dir_y == 1:
                max_y = max_y - len(word) + 1

            x = random.randint(min_x, max_x)
            y = random.randint(min_y, max_y)

            can_place = True
            for i, letter in enumerate(word):
                if wordsearch[y + i * dir_y][x + i * dir_x] not in [letter, None]:
                    can_place = False
                    break

            if can_place:
                placed = True

                for i, letter in enumerate(word):
                    wordsearch[y + i * dir_y][x + i * dir_x] = letter

    for line in wordsearch:
        for letter in line:
            if letter == None:
                print("- ", end="")
            else:
                print(letter + " ", end="")
        print()


if __name__ == '__main__':
    main()
