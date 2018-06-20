#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 14:07:39 2018

@author: mrpotatohead
"""
import numpy as np

class TTT:
    def __init__(self):
        self.board = ["-"] * 9
        self.player1 = "X"
        self.player2 = "O"
        self.player_list = [self.player1,self. player2]
        self.current_player = 0
      
    def reset_board(self):
        self.board = ["-"] * 9
        self.current_player = 0
        
    def switch_player(self):
        self.current_player = [1,0][self.current_player]
        
    def print_board(self):
        print(self.board[0:3])
        print()
        print(self.board[3:6])
        print()
        print(self.board[6:])
        
    def get_env(self):
        return self.board
    
    def get_legal_moves(self):
        legal_moves = []
        for i in range(len(self.board)):
            if self.board[i] == '-':
                legal_moves.append(i+1)
        return legal_moves
    
    def random_move(self):
        legal_moves = self.get_legal_moves()
        move = np.random.choice(legal_moves)
        return move
        
    def make_move(self, square, player):
        if self.board[square-1] == '-':
            self.board[square-1] = self.player_list[self.current_player]
            self.switch_player()
        else:
            return -3
        
    def select_move(self, human=True):
        if human:
            move = input("Select a square: ")
            return int(move)
        else:
            move = self.random_move()
            return move
        
    def check_win(self):
        win = False
        board = self.board
        for i in range(1, 10, 3):
            if board[i-1] == board[i] == board[i+1] and board[i] != '-':
                if self.current_player:
                    return 1
                return -2
        for i in range(1, 4):
            if board[i-1] == board[i+2] == board[i+5] and board[i-1] != '-':
                if self.current_player:
                    return 1
                return -2
        if board[0] == board[4] == board[8] and board[0] != '-':
            if self.current_player:
                return 1
            return -2
        if board[2] == board[4] == board[6] and board[2] != '-':
            if self.current_player:
                return 1
            return -2
        legal_moves = self.get_legal_moves()
        if not legal_moves:
            return -1
        return win
    
    def play_game(self, verbose=True):
        winner = False
        while winner not in [1,-1,-2]:
            if verbose:
                self.print_board()
            move = self.select_move(False)
            new_state = self.make_move(move, self.current_player)
            if new_state == -3:
                return new_state
            winner = self.check_win()
        if verbose:
            self.print_board()
        self.switch_player()
        return winner
            
    
T = TTT()

print(T.play_game())