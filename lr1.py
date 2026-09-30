import time
import os

# ЕРМОЛАЕВ ДЕНИС ДМИТРИЕВИЧ 559733

BLUE = '\u001b[44m'
RED = '\u001b[41m'
WHITE = '\u001b[47m'
BLACK = '\u001b[40m'
RESET = '\u001b[0m'
ERASE = '\x1B[2K'
BEGIN = '\x1B[1G'


# задание 1
def flag():
    pixel = '    '
    length = 10
    height = 9

    for i in range(height):
        if i < height // 3:
            print(RED + pixel * length + RESET)
        elif i < height // 3 * 2:
            print(WHITE + pixel * length + RESET)
        else:
            print(BLUE + pixel * length + RESET)


# задание 2
def uzor():
    pixel = '   '
    length = 9
    height = 9

    for i in range(height):
        if i == 0:
            print(BLACK + pixel * i + WHITE + pixel + BLACK + pixel * (length - i * 2 - 2) \
                  + WHITE + pixel + BLACK + pixel * i + BLACK + pixel * (length - 2) + WHITE + pixel + RESET)
        elif i < height // 2:
            print(BLACK + pixel * i + WHITE + pixel + BLACK + pixel * (length - i * 2 - 2) \
                  + WHITE + pixel + BLACK + pixel * i + BLACK + pixel * (i - 1) \
                  + WHITE + pixel + BLACK + pixel * (length - i * 2 - 2) + WHITE + pixel + BLACK + pixel * i + RESET)
        elif i == height // 2:
            print(BLACK + pixel * i + WHITE + pixel + BLACK + pixel * i + BLACK + pixel * (i - 1) \
                  + WHITE + pixel + BLACK + pixel * i + RESET)
        elif i > height // 2 and i != height - 1:
            print(BLACK + pixel * (length - i - 1) + WHITE + pixel + BLACK + pixel * (i * 2 - length) \
                  + WHITE + pixel + BLACK + pixel * (length - i - 1) \
                  + BLACK + pixel * (length - i - 2) + WHITE + pixel + BLACK + pixel * (i * 2 - length) \
                  + WHITE + pixel + BLACK + pixel * (length - i - 1) + RESET)
        else:
            print(WHITE + pixel + BLACK + pixel * (length - 2) \
                  + WHITE + pixel + BLACK + pixel * (length - 2) + WHITE + pixel + RESET)


# задание 3
def animation():
    pixel = '   '
    k = 0

    def x():
        pixel = '   '
        print(BLACK + pixel + WHITE + pixel * 3 + BLACK + pixel + RESET)
        print(WHITE + pixel + BLACK + pixel + WHITE + pixel + BLACK + pixel + WHITE + pixel + RESET)
        print(WHITE + pixel * 2 + BLACK + pixel + WHITE + pixel * 2 + RESET)
        print(WHITE + pixel + BLACK + pixel + WHITE + pixel + BLACK + pixel + WHITE + pixel + RESET)
        print(BLACK + pixel + WHITE + pixel * 3 + BLACK + pixel + RESET)

    def y():
        pixel = '   '
        print(BLACK + pixel + WHITE + pixel * 3 + BLACK + pixel + RESET)
        print(WHITE + pixel + BLACK + pixel + WHITE + pixel + BLACK + pixel + WHITE + pixel + RESET)
        print(WHITE + pixel * 2 + BLACK + pixel + WHITE + pixel * 2 + RESET)
        print(WHITE + pixel + BLACK + pixel + WHITE + pixel * 3 + RESET)
        print(BLACK + pixel + WHITE + pixel * 4 + RESET)

    def z():
        pixel = '   '
        print(BLACK + pixel * 5 + RESET)
        print(WHITE + pixel * 3 + BLACK + pixel + WHITE + pixel + RESET)
        print(WHITE + pixel * 2 + BLACK + pixel + WHITE + pixel * 2 + RESET)
        print(WHITE + pixel + BLACK + pixel + WHITE + pixel * 3 + RESET)
        print(BLACK + pixel * 5 + RESET)

    while True:
        if k == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            x()
            time.sleep(1)
            k += 1
        if k == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            y()
            time.sleep(1)
            k += 1
        if k == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            z()
            time.sleep(1)
            k = 0


# задание 4
def sequence():
    file = open('sequence.txt', 'r')
    odds = []
    evens = []
    k = 1
    for line in file:
        if k % 2 != 0:
            odds.append(abs(float(line)))
            k += 1
        else:
            evens.append(abs(float(line)))
            k += 1
    file.close()
    print(f'{BLUE}{" " * int(round(sum(odds), 2) / 20)}{RESET} {round(sum(odds), 2)/(round(sum(odds), 2) + round(sum(evens), 2)) * 100}%')
    print(f'{RED}{" " * int(round(sum(evens), 2) / 20)}{RESET} {round(sum(evens), 2)/(round(sum(odds), 2) + round(sum(evens), 2)) * 100}%')


# задание 5(доп задание)
def function():
    print('y = 2x')
    height = 20
    length = 10
    pixel = '   '
    for i in range(height, 0, -1):
        print(i if i > 9 else f'{i} ', '|', BLACK + pixel * (i // 2 - 1) \
              + WHITE + pixel + BLACK + pixel * (length - (i // 2 if i > 1 else 1)) + RESET)
    print("  ", ' ', '___' * 10)
    print(0, '   ', 1, '', 2, '', 3, '', 4, '', 5, '', 6, '', 7, '', 8, '', 9, 10, ' ')


flag()
uzor()
sequence()
function()
print('Уберите # с #animation() для 3 кадровой анимации')
#animation()
