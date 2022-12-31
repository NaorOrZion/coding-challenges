with open('input.txt', 'r') as file:
    data = file.read()
    answer = data[:4]

    if len(answer) == len(set(answer)):
        print(4)
        exit()

    for i in range(4, len(data)):
        # 'answer' should contain the 4 last repeated characters.
        # So if it's empty, there are 0 repeated characters.
        if len(answer[-4::]) == len(set(answer[-4::])):
            break

        answer += data[i]

    print(len(answer))