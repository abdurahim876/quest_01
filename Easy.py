import random
digit = random.randint(0,100)
while True:
    s = input("введите число: ")
    s = int(s)
    if digit == s:
        print("угадал!")
        break
    elif digit > s:
        print("больше")
    else:
        print("меньше")







