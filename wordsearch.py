def main():
    width = int(input("Please enter the width of the wordsearch: "))
    height = int(input("Please enter the height of the wordsearch: "))

    words = []

    with open("wordsearch.txt", "r") as file:
        for word in file.readlines():
            words.append(word.strip())

    wordsearch = []


if __name__ == '__main__':
    main()
