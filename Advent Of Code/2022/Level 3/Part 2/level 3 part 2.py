with open('input.txt', 'r') as file:
    data = file.read().split('\n')
    abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    items = []
    sum = 0
    counter = 0

    while counter < len(data)-2:
        common_character = ''.join(set(data[counter]).intersection(data[counter+1], data[counter+2]))
        sum += abc.index(common_character) + 1
        counter += 3

    print(sum)