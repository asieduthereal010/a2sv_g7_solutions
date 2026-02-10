for _ in range(int(input())):
    word = input()
    word_len = len(word)
    if word_len > 10:
        print(word[0]+f"{word_len-2}"+word[word_len-1])
    else: 
        print(word)
