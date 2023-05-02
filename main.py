# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    answer = '5312'
    guess = '4215'

    bulls, cows = count_logic(answer,guess)
    print(bulls,cows)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
