from collections import defaultdict


file = open('input.txt', 'r')
lines = file.read().split('\n')
file.close()


def stack_line():
    '''
    The function returns the line index and line length, 
    which contains the stack's numbers
    '''

    for index, line in enumerate(lines):
        if line.find(' 1') != -1:
            line_index = index
            line_length = len(line)
            break

    return line_length, line_index


def create_stacks():
    '''
    Example for this input:
            [D]    
        [N] [C]    
        [Z] [M] [P]
         1   2   3

    e.i: [stack_number]: [line_index-1][which letter should be pushed to the top of the list]
    e.g: 1: ['Z'], 2: ['M'], 3:['P']
    e.g: 1: ['Z', 'N'], 2: ['M', 'C'], 3:['P']
    e.g: 1: ['Z', 'N'], 2: ['M', 'C', 'D'], 3: ['P']
    '''

    line_length, line_index = stack_line()
    letter_index = 1
    stack_number = 1
    stacks = defaultdict(list)   

    while line_index > 0:
        stacks[stack_number].append(lines[line_index-1][letter_index])

        # If a blank space was inserted then pop it from the list
        if lines[line_index-1][letter_index] == ' ':
            stacks[stack_number].pop()

        stack_number += 1
        letter_index += 4

        if letter_index > line_length:
            stack_number = 1
            letter_index = 1
            line_index -= 1
    
    return stacks


def calculate_stacks(stacks):
    _, line_index = stack_line()
    instructions_index = line_index+2
    instructions = lines[instructions_index:]

    for instruction in instructions:
        line = instruction.split(" ")
        crates_to_pop = int(line[1])
        crate_taken = int(line[3])
        crate_given = int(line[5])

        for _ in range(crates_to_pop):
            stacks[crate_given].append(stacks[crate_taken].pop())

    return who_is_on_top(stacks)


def who_is_on_top(stacks):
    top = ""

    for i in range(1, len(stacks)+1):
        top += stacks[i][-1]

    return top


def main():
    stacks = create_stacks()
    print(calculate_stacks(stacks))


if __name__ == '__main__':
    main()



        

