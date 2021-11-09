

from minimax import Minimax
from util import Util


class Game:

    def __init__(self):
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]    
        self.turn = ''
        self.moves = 0
        self.ai_player = Minimax()
        
    
    def show_board(self):
        index = 1
        print("  ____________________")
        for i in range(0, 3):
            for x in range(0, 3):
                current = self.board[i][x]
                if current != 0:
                    if current == 1:
                        print(" | ", "O", end=' | ')
                    else:
                        print(" | ", "X", end=' | ')
                else:
                    print(" | ", index, end=' | ')
                index = index + 1
            print("")
        print("  ____________________")
        print("")

    def play(self, offset, ai = False):
        if ai:
            self.board[offset[0]][offset[1]] = self.translate_turn(self.turn)
            self.update_turn()
            return True
        move = self.translate_move(offset)
        if move == None:
            return False
        if self.board[move[0]][move[1]] == 0:
            self.board[move[0]][move[1]] = self.translate_turn(self.turn)
            self.update_turn()
            return True
        return False

    def translate_turn(self, move):
        if move == 'X':
            return -1
        return 1

    def update_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'
        self.moves = self.moves + 1

    def start(self):
        answer = input("Você deseja começar? [y/n]")
        if answer == 'y':
            self.turn = 'X'
        else:
            self.turn = 'O'
        self.show_board()
        while True:
            if self.turn == 'O':
                move = self.ai_player.ai_turn(self.board)
                self.play(move, True)
                print("Jogada do Computador")
            else:
                move = input("Entre com a jogada: ")
                valid = self.play(move)
                if not valid:
                    print("Jogada Inválida")
            self.show_board()
            if self.moves == 9:
                print("Empate")
                break
            result = Util.check_game(self.board)
            if result != None:
                if self.turn == 'X':
                    winner = 'O'
                else:
                    winner = 'X'
                print("Jogador ", winner, " venceu")
                break

    def translate_move(self, move):
        moves = {
            '1': (0, 0),
            '2': (0, 1),
            '3': (0, 2),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '7': (2, 0),
            '8': (2, 1),
            '9': (2, 2)
        }
        if move in moves:
            return moves[move]
        return None
	    