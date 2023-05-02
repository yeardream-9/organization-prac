


def count_logic(answer,guess):
    bulls = 0
    cows = 0
    for a_index, amswer_num in enumerate(answer):
        for g_index, guess_num in enumerate(guess):
            if amswer_num == guess_num:
                if a_index == g_index:
                    bulls += 1
                else:
                    cows += 1
    return bulls,cows