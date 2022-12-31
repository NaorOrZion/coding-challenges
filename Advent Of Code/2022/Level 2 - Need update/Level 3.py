with open('input.txt', 'r') as file:
    data = file.read().split('\n')
    sum_game = 0

    def calc_win(chr_my_turn, chr_opp_turn):
        my_turn = ord(chr_my_turn) - 23 # 88(X) - 23 = 65(A)
        opp_turn = ord(chr_opp_turn)

        if (my_turn - opp_turn) == 0:
            return 3

        if chr_my_turn == 'X':
            if (my_turn - opp_turn) == -1:
                return 0
            elif (my_turn - opp_turn) == -2:
                return 6

        if chr_my_turn == 'Y':
            if (my_turn - opp_turn) == 1:
                return 6
            elif (my_turn - opp_turn) == -1:
                return 0

        if chr_my_turn == 'Z':
            if (my_turn - opp_turn) == 1:
                return 6
            elif (my_turn - opp_turn) == 2:
                return 0

        return 3
    
    for game in data:
        my_turn = game[-1]
        opp_turn = game[0]
        
        if my_turn == 'X': # NEED LOSE
            if opp_turn == 'A':
                sum_game += calc_win('Z', opp_turn)
                sum_game += 3
            if opp_turn == 'B':
                sum_game += calc_win('X', opp_turn)
                sum_game += 1
            if opp_turn == 'C':
                sum_game += calc_win('Y', opp_turn)
                sum_game += 2
        if my_turn == 'Y': # NEED DRAW
            if opp_turn == 'A':
                sum_game += calc_win('X', opp_turn)
                sum_game += 1
            if opp_turn == 'B':
                sum_game += calc_win('Y', opp_turn)
                sum_game += 2
            if opp_turn == 'C':
                sum_game += calc_win('Z', opp_turn)
                sum_game += 3
        if my_turn == 'Z': # NEED WIN
            if opp_turn == 'A':
                sum_game += calc_win('Y', opp_turn)
                sum_game += 2
            if opp_turn == 'B':
                sum_game += calc_win('Z', opp_turn)
                sum_game += 3
            if opp_turn == 'C':
                sum_game += calc_win('X', opp_turn)
                sum_game += 1


    print(sum_game)