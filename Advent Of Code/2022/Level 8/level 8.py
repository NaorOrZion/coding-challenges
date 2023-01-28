with open(r"input.txt", 'r') as file:
    data = file.read().split('\n')
    data = [[int(j) for j in i] for i in data]
    visible = len(data[0])*2 + (len(data)-2)*2  # Calculate sum of all edges - 16


    def check_col(tree_house, row1, col1):
        is_visible_ttb = True  # Top to Bottom
        is_visible_btt = True  # Bottom to Top

        for row in range(row1):
            if data[row][col] >= tree_house:
                    is_visible_ttb = False

        for row in range(row1+1, len(data)): 
            if data[row][col] >= tree_house:
                is_visible_btt = False

        return is_visible_ttb or is_visible_btt
    

    for row in range(1, len(data)-1):
        for col in range(1, len(data[0])-1):
            max_ltr = max(data[row][:col])  # Find max height of a tree from left edge to tree house
            max_rtl = max(data[row][col+1:])  # Find max height of a tree from tree house to right edge

            # Even if one of the maximum height trees is taller then the tree house height,
            # the tree house is visible.
            if max_ltr < data[row][col] or max_rtl < data[row][col]:
                visible += 1
            # Checks the same thing but on columns
            elif check_col(data[row][col], row, col):
                visible += 1


    print(visible)