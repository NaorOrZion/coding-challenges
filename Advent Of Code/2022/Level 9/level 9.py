# Day 9: https://adventofcode.com/2022/day/9

tx, ty = 0, 0
hx, hy = 0, 0


def main():
    print("Advent of Code - Day 9")
    file_task_1 = open('input.txt', 'r')
    file_task_2 = open('input.txt', 'r')
    task_1(file_task_1)
    task_2(file_task_2)


def touching():
    return abs(tx-ty) <= 1 and abs(ty - hy) <= 1


def task_1(file):
    data = file.read().split("\n")
    print(data)


def task_2(file):
    pass


if __name__ == "__main__":
    main()