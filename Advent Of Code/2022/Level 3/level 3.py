with open('input.txt', 'r') as file:
    data = file.read().split('\n')
    abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    items = []
    sum = 0

    for item in data:
        comp = []
        firstpart = item[:len(item)//2]
        secondpart = item[len(item)//2:]
        common_character = ''.join(set(firstpart).intersection(secondpart))
        sum += abc.index(common_character) + 1

    print(sum)