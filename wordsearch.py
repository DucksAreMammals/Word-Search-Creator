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
        dir_x = random.randint(-1, 1)
        dir_y = random.randint(-1, 1)

        if dir_x == 0 and dir_y == 0:
            if random.random() > 0.5:
                dir_x = random.choice([1, -1])
            else:
                dir_y = random.choice([1, -1])

        print(dir_x, dir_y)

    for line in wordsearch:
        for letter in line:
            print(str(letter) + " ", end="")
        print()


if __name__ == '__main__':
    main()
