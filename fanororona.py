#
# AI that learns to play Tic Tac Toe using
#        reinforcement learning
#                (MCTS)
#

# packages
from copy import deepcopy
import traceback
from mcts import *

pairs = [(i, j) for i in range(5) for j in range(5)]
dict_dir = {'no':(0,0),'up':(-1,0),'down':(1,0), 'left':(0,-1),'right':(0,1),'upleft':(-1,-1),'upright':(-1,1),'downleft':(1,-1),'downright':(1,1)} 
dict_dir_no_diagonal = {'no':(0,0),'up':(-1,0),'down':(1,0), 'left':(0,-1),'right':(0,1)} 

# Tic Tac Toe board class
class Board():
    # create constructor (init board class instance)
    def __init__(self, board=None, scan=True):
        # define players
        self.player_1 = 'x'
        self.player_2 = 'o'
        self.empty_square = '.'
        self.path = []
        self.restricted_position = []
        self.all_available_moves = []
        self.last_move = None
        
        # define board position
        self.position = {}
        
        # init (reset) board
        self.init_board()
        if scan:
            self.all_moves()
        
        # create a copy of a previous board state if available
        if board is not None:
            self.__dict__ = deepcopy(board.__dict__)
    
    # init (reset) board
    def init_board(self, n=5):
        # fill first two rows with 'x'
        for row in range(2):
            for col in range(n):
                self.position[row, col] = self.player_1
        
        # fill first two columns of the third row with 'x'
        for col in range(2):
            self.position[2, col] = self.player_1
        
        # fill last two rows with 'o'
        for row in range(n-2, n):
            for col in range(n):
                self.position[row, col] = self.player_2
        
        # fill the middle row
        self.position[2,0] =  self.player_2
        self.position[2,1] =  self.player_1
        self.position[2,2] = self.empty_square
        self.position[2,3] =  self.player_2
        self.position[2,4] = self.player_1
    # Get all available direction from a position(tuple) on a given board

    def available_direction(self, position):
        direction = dict_dir.copy()

        #restrict diagonal move on some position of the board
        if pairs.index(position) % 2 == 1:  # Even-indexed position
            direction = dict_dir_no_diagonal.copy()
        
        #player have to move if the previous action was not a taking move
        if not self.path:
            del direction['no']

        return direction

    # get all valid move from a given board
    def all_moves(self):

        all_valid_moves = []

        # determine available starting positions for generating moves.
        if self.path:
            # if the previous move was a capturing move, only the piece that made the capture can be moved.
            available_position = [self.path[-1]]
        else: 
            #else every position can be considered
            available_position = self.position.keys()

        # check all available position 
        for x , y in available_position:
            DIRECTION = self.available_direction((x,y)).items()
            # make sure the posistion contain a player 1 piece
            if self.position[x,y] == self.player_1:
                #check all direction
                for dir, (dx,dy)  in DIRECTION:
                    #handle the 'no move' option
                    if dir == 'no':
                        all_valid_moves.append([x,y,dir,'n'])

                    else:
                        # calculate destination position given starting pos and direction
                        x_dest = x + dx
                        y_dest = y + dy
                        # check for valid movement conditions.
                        if (x_dest, y_dest) in self.position.keys() and (x_dest, y_dest) not in self.path and (x_dest, y_dest) not in self.restricted_position  and self.position[x_dest,y_dest] == self.empty_square: 

                            # check forward and backward capturing possibilities.
                            x_f = x + 2 * dx
                            y_f =  y + 2 * dy
                            x_b = x - dx
                            y_b = y - dy

                            if (x_f,y_f) in self.position.keys() and self.position[x_f,y_f] == self.player_2:
                                    all_valid_moves.append([x, y, dir, 'f'])
                            elif (x_b,y_b) in self.position.keys() and self.position[x_b,y_b] == self.player_2:
                                    all_valid_moves.append([x, y, dir, 'b'])
                            else:
                                # handle regular move.
                                all_valid_moves.append([x,y,dir,'m'])

        # determine if there are any capturing moves available.
        taking_moves_availables = any(move[3] in ('b', 'f') for move in all_valid_moves)

        # apply game rules

        if not self.path:
            if taking_moves_availables:
                # capture moves are available, you must choose one of them.
                self.all_available_moves = [move for move in all_valid_moves if move[3] in ('b', 'f')]
            else:
                # you must move one of your pieces in a single direction. (you have to move)
                self.all_available_moves =  all_valid_moves
        else:
            # if the last move was a capture, you can choose not to make a move.
            self.all_available_moves = [move for move in all_valid_moves if move[3] in ('b', 'f', 'n')]


    # check if the move is valid by returning its index if it exists in self.available_moves.
    def check_valid(self, start_row, start_col, direction, target):
        if [start_row, start_col,direction,target] in  self.all_available_moves:
            return self.all_available_moves.index([start_row, start_col,direction,target])
        else:
            return -1

    # handle removing the pieces taken by capture
    def take(self, start_row,start_col, direction,target):

        # get the position of the first target
        if target == 'f':
            mult = 1
            tar_row = start_row + 2 * dict_dir[direction][0]
            tar_col = start_col + 2 * dict_dir[direction][1]
        else:
            mult = -1
            tar_row = start_row -  dict_dir[direction][0]
            tar_col = start_col - dict_dir[direction][1]

        #loop to remove all target
        while (tar_row, tar_col) in self.position.keys() and self.position[tar_row, tar_col] == self.player_2:

            self.position[tar_row, tar_col] = self.empty_square
            tar_row += mult * dict_dir[direction][0]
            tar_col += mult * dict_dir[direction][1]


    #
    def make_move(self, start_row, start_col, direction, target):

        board = Board(self, False)

        res = self.check_valid(start_row, start_col, direction, target)

        if res == -1:
            return board
        else:
            #Move
            x_dest = start_row + dict_dir[direction][0]
            y_dest = start_col + dict_dir[direction][1]


            board.position[start_row, start_col] = self.empty_square
            board.position[x_dest, y_dest] = self.player_1
            board.last_move = [start_row, start_col, direction, target]

            if target not in ['m','n']:
                if self.path:
                    #restrict player to not move in the same direction twice
                    x_restr = start_row + 2 * dict_dir[direction][0]
                    y_restr = start_col + 2 * dict_dir[direction][1]
                    board.restricted_position = [(x_restr,y_restr)]

                    #restrict player to not make a move on his previous path
                    board.path.append((x_dest,y_dest))

                else:
                    #restrict player to not make a move on his previous path
                    board.path.append((start_row,start_col))
                    board.path.append((x_dest,y_dest))
                
                #remove the pieces from the board
                board.take(start_row, start_col, direction, target)
    
        # Switch players
        #switch and reset board.path if the previous move was not a taking move
        if board.path and direction != 'no':
            pass
        else:
            (board.player_1, board.player_2) = (board.player_2, board.player_1)
            board.path = []
            board.restricted_position = []

        #direct switch and reset if the last move was a taking move but no taking move is available on the next
        board.all_moves()

        # if len(board.all_available_moves) == 1 and board.all_available_moves[0][2]== 'no':
        #     (board.player_1, board.player_2) = (board.player_2, board.player_1)
        #     board.path = []
        #     board.all_moves()
        #     return board
        
        return board
    
    
    # get whether the game is drawn
    def is_draw(self):
        
        return False
    
    # get whether the game is won
    def is_win(self):
       if self.player_2 not in self.position.values():   
        return  True
       else:
        return False 
    
    # generate legal moves to play in the current position
    def generate_states(self):

        self.all_moves()
        return [self.make_move(move[0],move[1],move[2],move[3]) for move in self.all_available_moves] #lists of boards
    
    # main game loop
    # def game_loop(self):
        
    #     # print board
    #     print(self)

    def game_loop(self):
        print('\nFanorona by Aina Herimam\n')
        print('Type "exit" to quit the game')
        print('  Move format: x,y,direction,target')
        print('     x: row')
        print('     y: col')
        print('     direction: up, down, left, right, upleft, upright, downleft, downright')
        print('     target: f(forward capture)  b(backward capture)  n(no move),  m(move only)')
        print('\n Exemple: 2,3,upleft,m')
        
        # print board
        print(self)
        
        # create MCTS instance
        mcts = MCTS()
                
        # game loop
        while True:
            #print all available move
            print("Available moves: " + "   -   ".join([",".join(map(str, move)) for move in self.all_available_moves]))
            # get user input
            user_input = input('> ')
        
            # escape condition
            if user_input == 'exit': break
            
            # skip empty input
            if user_input == '': continue
            
            try:
                # parse user input (move format [row, col, dir, tar]
                row = int(user_input.split(',')[0]) 
                col = int(user_input.split(',')[1]) 
                dir = user_input.split(',')[2]
                tar = user_input.split(',')[3]

                # check move legality
                if self.check_valid(row,col,dir,tar) == -1:
    
                    print(f' Illegal move!- {[row, col, dir, tar]}')
                    continue

                # make move on board
                self = self.make_move(row, col, dir, tar)
                print(f'Player 1 take the move {[row, col, dir, tar]}')
                
                # print board
                print(self)
                while self.player_1 == 'o':
                
                    # search for the best move
                    best_move = mcts.search(self)
                    
                    # legal moves available
                    try:
                        # make AI move here
                        self = best_move.board

                        print(f'Player 2 take the move {self.last_move}')
                    
                    # game over
                    except:
                        pass
                
                    # print board
                    print(self)
                    
                    # check if the game is won
                    if self.is_win():
                        print('player "%s" has won the game!\n' % self.player_2)
                        break
            
            except Exception as e:
                print('  Error:', e)
                print('  Illegal command!')
                print(traceback.print_exc())


    # print board state
    def __str__(self):
        # define board string representation
        board_string = f'  0 1 2 3 4\n' +  '0'
        # board_string = ''
        
        # loop over board rows
        for row in range(5):
            # loop over board columns
            for col in range(5):
                # add each square's state to the string
                board_string += f' {self.position[row, col]}'
            
            # add a new line at the end of each row
            board_string += '\n' + str(row+1)
        
        # prepend the current player to move
        board_string = (
            f'\n--------------\n "{self.player_1}" to move:\n--------------\n\n'
            + board_string
        )
        
        # return the full board string
        return board_string[:-1]

# main driver
if __name__ == '__main__':
    # create board instance
    board = Board()
    board.game_loop()



        
    

    
    
    
    
    
    
    
