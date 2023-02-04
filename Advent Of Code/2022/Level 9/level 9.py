# Day 9: https://adventofcode.com/2022/day/9

tx, ty = 0, 0
hx, hy = 0, 0
tail_visited = {(0, 0)}


def move_tail(movex, movey):
    global tail_visited
    global tx, ty

    # x and y differences
    x_diff = hx - tx
    y_diff = hy - ty
    print("x_diff y_diff: ", x_diff, y_diff)

    # First situation
    if x_diff == 1 and y_diff == 2:
        tx += 1
        ty += 1

    # Second situation
    elif x_diff == -2 and y_diff == 1:
        tx -= 1
        ty += 1

    # Third situation
    elif x_diff == -1 and y_diff == -2:
        tx -= 1
        ty -= 1

    # Fourth situation
    elif x_diff == 2 and y_diff == -1:
        tx += 1
        ty -= 1
    
    # Fifth situaion - regular movement(row/column)
    else:
        tx += movex
        ty += movey

    tail_visited.add((tx, ty))


def move_head(action, steps):
    global hx, hy
    global tx, ty

    if action == "R":
        for _ in range(steps):
            hx += 1
            if not touching():
                move_tail(1, 0)
            print("tx ty: ", tx, ty)
            print("================")

    if action == "L":
        for _ in range(steps):
            hx -= 1
            if not touching():
                move_tail(-1, 0)
            print("tx ty: ", tx, ty)
            print("================")

    if action == "U":
        for _ in range(steps):
            hy += 1
            if not touching():
                move_tail(0, 1)
            print("tx ty: ", tx, ty)
            print("================")

    if action == "D":
        for _ in range(steps):
            hy -= 1
            if not touching():
                move_tail(0, -1)
            print("tx ty: ", tx, ty)
            print("================")    


def touching():
    return abs(tx - hx) <= 1 and abs(ty - hy) <= 1


def task_1(file):
    data = file.read().split("\n")

    for order in data:
        action = order[0]
        steps = int(order[-1])
        move_head(action, steps)

    #print(tail_visited)
    print(len(tail_visited))


def task_2(file):
    pass


def main():
    print("Advent of Code - Day 9")
    file_task_1 = open('input.txt', 'r')
    file_task_2 = open('input.txt', 'r')
    task_1(file_task_1)
    task_2(file_task_2)


if __name__ == "__main__":
    main()