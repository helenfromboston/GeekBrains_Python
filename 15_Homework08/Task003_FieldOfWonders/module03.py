def g_check(guess, word, hidden):
    new_word = ''
    L = len(word)
    for i in range(L):
        if word == guess:
            new_word = word
        elif hidden[i] != '*':
            new_word += hidden[i]
        elif word[i] == guess:
            new_word += guess
        else:
            new_word += '*'
    return new_word