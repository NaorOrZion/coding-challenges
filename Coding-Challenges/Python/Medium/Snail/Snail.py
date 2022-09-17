def snail(snail_map):
    if len(snail_map[0]) == 0:
        return []
    
    #middle line/row means the position of the middle number in the array([y][x])
    length = len(snail_map)
    middle_line = int(length/2)
    middle_row = int(length/2) - 1 if length % 2 == 0 else int(length/2)
    
    line = 0
    row = 0
    flag = 0
    snail_list = []

    #Because I will do a snail action, my bounderies will get samller with each full circular action
    index_end_row = 1
    index_end_line = 1
    index_start_row = 0
    index_start_line = 0
    
    #Don't stop the iteration until getting to the middle element
    while line != middle_line or row != middle_row:
        #Append left to right items
        if flag == 0:
            if row != length - index_end_row:
                snail_list.append(snail_map[line][row])
                row += 1
            elif row == length - index_end_row:
                snail_list.append(snail_map[line][row])
                index_end_row += 1
                index_start_line += 1
                flag = 1
                
        #Append upper to bottom
        elif flag == 1:
            if line != length - index_end_line:
                line += 1
                snail_list.append(snail_map[line][row])
            elif line == length - index_end_line:
                index_end_line += 1
                flag = 2
                
        #Append right to left
        elif flag == 2:
            if row != 0 + index_start_row:
                row -= 1
                snail_list.append(snail_map[line][row])
            elif row == 0 + index_start_row:
                index_start_row += 1
                flag = 3
        
        #Append bottom to upper
        elif flag == 3:
            if line != 0 + index_start_line:
                line -= 1
                snail_list.append(snail_map[line][row])            
            elif line == 0 + index_start_line:                
                row += 1
                flag = 0
    
    if length%2 != 0:
        snail_list.append(snail_map[middle_line][middle_row])
    
    return snail_list