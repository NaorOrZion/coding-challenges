def strip_comments(strng, markers):
    new_string = strng.split("\n")
    print(new_string)
    for index_line, line in enumerate(new_string):
        for index_char, char in enumerate(line):
            if char in markers and index_char != 0:
                new_string[index_line] = line[:index_char-1]
                break
            elif char in markers and index_char == 0:
                new_string[index_line] = ''
                break
    for i, value in enumerate(new_string):
        if value in markers:
            new_string[i] = ''
        if value == ' ':
            new_string[i] = ''
    print(new_string)
    return '\n'.join(new_string)