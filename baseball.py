import random

secret_number = ''.join(random.sample('0123456789', 4))
print("Bulls and Cows - Guess the 4 number")

if input == answer:
    print('축하합니다. 정답입니다!')
else:
    print('정답이 아닙니다!')

