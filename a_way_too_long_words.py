def abbreviate_word(word):
    if len(word) > 10:
        print(word[0] + str(len(word) - 2) + word[-1])
    else:
        print(word)

def main():
    number_of_words = int(input())
    words_arr = []
    for i in range(number_of_words):
        word = input().strip()
        words_arr.append(word)
    for word in words_arr:
        abbreviate_word(word)


if __name__ == '__main__':
    main()