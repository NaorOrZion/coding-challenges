with open('input.txt', 'r') as file:
    data = file.read().split('\n')
    data.append("")
    num_of_elves = data.count('')
    count_elves = 0
    counter = 0
    sum_last_three = 0
    elves_calories = [0]

    while count_elves < num_of_elves:
        if data[counter] != '':
            elves_calories[count_elves] += int(data[counter])
        else:
            count_elves += 1
            elves_calories.append(0)

        counter += 1

    for i in range(3):
        sum_last_three += max(elves_calories)
        elves_calories.remove(max(elves_calories))

    print(sum_last_three)
