with open('input.txt', 'r') as file:
    data = file.read()
    answer = data[:14]

    if len(answer) == len(set(answer)):
        print(14)
        exit()

    for i in range(14, len(data)):
        # 'answer' should contain the 4 last repeated characters.
        # So if it's empty, there are 0 repeated characters.
        if len(answer[-14::]) == len(set(answer[-14::])):
            break

        answer += data[i]

    print(len(answer))