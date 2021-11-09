from util import Util
import copy
import sys

class Minimax:

    def __init__(self):
        self.human = -1
        self.ai = +1

    # Função de utilidade
    def fit(self, state):
        result = Util.check_game(state)
        value = 0
        # Verifica se chegou a vitória de algum jogador e atribui um valor baseado no Min e Max
        if result == 1:
            value = +1
        elif result == -1:
            value = -1
        return value

    # Jogada do computador
    def ai_turn(self, board):
        # Faz uma cópia pra não alterar o estado do objeto passado
        board_copy = copy.deepcopy(board)
        # Profunidade corresponde a quantidade de células vazias no tabuleiro
        level = len(self.empty_cells(board))
        # Cálcula a próxima jogada com o algoritmo Minimax
        play = self.minimax(board_copy, self.ai, level)
        # Retorna uma tupla com os índices da melhor jogada para o computador
        return (play[0], play[1])

    # Método utilitário que retorna células vazias no tabuleiro
    def empty_cells(self, board):
        empty_cells = []
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == 0:
                    empty_cells.append([i, j])
        return empty_cells
    
    # Algoritmo Minimax que procura soluções ótimas a partir do tabuleiro passado
    def minimax(self, board, player, level):
        # Definiu-se que a IA é o Min, logo começa como melhor valor o menor valor possível
        if player == self.ai:
            result = [-1, -1, -sys.maxsize - 1]
        # Definiu-se que o jogador é Max, logo começa como melhor valor o maior valor possível
        else:
            result = [-1, -1, sys.maxsize]
        # Se chegar a profunidade igual a zero é um nó folha ou
        # Se chegar com a vitória de algum dos lados usa a função de utilidade para avaliar a jogada e retorna
        if level == 0 or Util.check_game(board) != None:
            value = self.fit(board)
            return [-1, -1, value]
        # Avança as jogadas para cada célula vazia do tabuleiro
        for value in self.empty_cells(board):
            row, col = value[0], value[1]
            # Atribui a jogada a célula vazia
            board[row][col] = player
            # Chama próximo estado avançando a árvore de estado em 1 e o estado atual do tabuleiro
            value = self.minimax(board, -player, level - 1)
            board[row][col] = 0
            value[0] = row
            value[1] = col
            # Valor Max
            if player == self.ai:
                # Verifica se o score recebido é melhor do que atual melhor, nesse caso maior
                if value[2] > result[2]:
                    result = value
            # Valor Min
            else:
                # Verifica se o score recebido é melhor do que atual melhor, nesse caso menor
                if value[2] < result[2]:
                    result = value  
        return result