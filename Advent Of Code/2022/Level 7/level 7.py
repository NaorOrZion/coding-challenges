with open('input.txt', 'r') as file:
    data = file.read().split('\n')
    sum = 0
    directories = {}
    # max = 100,000
    below_max = []
    is_above_max = False

    print(data)

    for item in data:
        if item.isnumeric():
            sum += int(item)

    print(sum)