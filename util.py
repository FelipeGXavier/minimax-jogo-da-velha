class Util:

    @staticmethod
    def check_game(board):
        win_conditions = [
            ((0,0), (0,1), (0,2)),
            ((1,0), (1,1), (1,2)),
            ((2,0), (2,1), (2,2)),
            ((0,0), (1,0), (2,0)),
            ((0,1), (1,1), (2,1)),
            ((0,2), (1,2), (2,2)),
            ((0,0), (1,1), (2,2)),
            ((2,0), (1,1), (0,2))
        ]
        for condition in win_conditions:
            first_pos = condition[0]
            second_pos = condition[1]
            third_pos = condition[2]

            first_pos_val = board[first_pos[0]][first_pos[1]]
            second_pos_val = board[second_pos[0]][second_pos[1]]
            third_pos_val = board[third_pos[0]][third_pos[1]]

            if ([first_pos_val, second_pos_val, third_pos_val] != [0, 0, 0] 
                and first_pos_val == second_pos_val  and second_pos_val == third_pos_val):
                return board[first_pos[0]][first_pos[1]]
        return None