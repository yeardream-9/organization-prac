# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import count_logic




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    answer = '5312'
    guess = '4215'

    bulls, cows = count_logic.count_logic(answer,guess)
    print("Bulls:"+str(bulls)+" Cows:"+str(cows))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
