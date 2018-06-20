#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 14:07:39 2018

@author: mrpotatohead
"""
import numpy as np


class TTT:
    def __init__(self, p1, p2):
        self.board = [0] * 9
        self.player1 = p1
        self.player2 = p2
        self.player_list = [self.player1,self. player2]
        self.current_player = 0
      
    def reset(self):
        self.board = [0] * 9
        self.current_player = 0
        return np.array(self.board)
        
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
            if self.board[i] == 0:
                legal_moves.append(i+1)
        return legal_moves
    
    def random_move(self):
        legal_moves = self.get_legal_moves()
        move = np.random.choice(legal_moves)
        return move
        
    def make_move(self, square, player):
        if self.board[square-1] == 0:
            self.board[square-1] = self.player_list[self.current_player].symbol
            self.switch_player()
        else:
            return -3
        
    def select_move(self):
        player = self.player_list[self.current_player]
        if player.human:
            move = input("Select a square: ")
            return int(move)
        else:
            move = self.random_move()
            return move
        
    def check_win(self):
        win = 0
        board = self.board
        for i in range(1, 10, 3):
            if board[i-1] == board[i] == board[i+1] and board[i] != 0:
                if self.current_player:
                    return 1
                return -2
        for i in range(1, 4):
            if board[i-1] == board[i+2] == board[i+5] and board[i-1] != 0:
                if self.current_player:
                    return 1
                return -2
        if board[0] == board[4] == board[8] and board[0] != 0:
            if self.current_player:
                return 1
            return -2
        if board[2] == board[4] == board[6] and board[2] != 0:
            if self.current_player:
                return 1
            return -2
        legal_moves = self.get_legal_moves()
        if not legal_moves:
            return -1
        return win
    
    def step(self, action):
        if self.player_list[self.current_player].human:
            move = action
            new_state = self.make_move(move, self.current_player)
            if new_state == -3:
                return new_state
            winner = self.check_win()
        else:
            move = self.random_move()
            new_state = self.make_move(move, self.current_player)
            winner = self.check_win()
        if winner in [1,-1,-2]:
            return new_state, winner, True, "Game over"
        return new_state, winner, False, "Game Continues"
    
    def play_game(self, verbose=True):
        winner = False
        while winner not in [1,-1,-2]:
            if verbose:
                self.print_board()
            move = self.select_move()
            new_state = self.make_move(move, self.current_player)
            if new_state == -3:
                return new_state
            winner = self.check_win()
        if verbose:
            self.print_board()
        self.switch_player()
        return winner
     
        
#p1 = Player(True,"X")
#p2 = Player(False,"O")
#    
#T = TTT(p1,p2)
#
#print(T.play_game())