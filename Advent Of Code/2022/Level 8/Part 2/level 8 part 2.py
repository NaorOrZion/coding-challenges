with open(r"input.txt", 'r') as file:
    data = file.read().split('\n')
    data = [[int(j) for j in i] for i in data]
    scenic_score = 1
    max_scenic_score = 0


    # Calculate scenic distance
    def calc_scenic_dist(trees, tree_house):
        distance = 0

        for tree in trees:
            if tree < tree_house:
                distance += 1
            else:
                distance += 1
                break
        
        return distance


    for row in range(len(data)):
        for col in range(len(data[0])):
            # Calculating the lists which will define the scenic distance
            list_row_rtl = (data[row][:col])[::-1]  # Tree house to left
            list_row_ltr = data[row][col+1:]  # Tree house to right
            list_col_ttb = ([i[col] for i in data[:row]])[::-1]  # Top to tree house
            list_col_btt = [i[col] for i in data[row+1:]]  # Bottom to tree house

            # Multiplying the sum of all scenic distance 
            scenic_score *= calc_scenic_dist(list_row_rtl, data[row][col])  # List tree house to left
            scenic_score *= calc_scenic_dist(list_row_ltr, data[row][col])  # List tree house to right
            scenic_score *= calc_scenic_dist(list_col_ttb, data[row][col])  # List top to tree house
            scenic_score *= calc_scenic_dist(list_col_btt, data[row][col])  # List bottom to tree house

            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

            scenic_score = 1

    print(max_scenic_score)