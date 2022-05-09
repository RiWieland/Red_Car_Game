
#import numpy as np
import random

# to do:
# how an instance prints uses its onwn function (see def execute_stop())


# Add:
# Board-logic:
# - Cars not over each other

# Main:
# - create board
# - create all cars -> dict with definitions
# - place cars on it
# - calculate evercol posible state from the current one

#Create placoler board
def create_board(length=int, weigth=int) -> list:

    placoler_board = []

    for placoler_row in range(length):
        placoler_board.append([])
        for placoler_col in range(width):
            placoler_board[placoler_row].append('.')

    return placoler_board

#Print placoler board
def print_board(placoler_board: list):
    for placoler_row in placoler_board:
        print(" ".join(placoler_row))
    
# Board:
length = 8
width = 9

# Car-definitions
car_dict = {
    0: {"row": 1, "col": 3, "length": 3, "orientation": 'v'},
    1: {"row": 4, "col": 5, "length": 2, "orientation": 'h'},
    2: {"row": 7, "col": 3, "length": 4, "orientation": 'h'},
    3: {"row": 0, "col": 3, "length": 4, "orientation": 'h'},
    4: {"row": 1, "col": 4, "length": 4, "orientation": 'v'},
    5: {"row": 5, "col": 2, "length": 3, "orientation": 'h'},
    6: {"row": 6, "col": 2, "length": 5, "orientation": 'h'},
    7: {"row": 3, "col": 0, "length": 5, "orientation": 'v'},
}

car_red = {
    'R': {"row": 1, "col": 6, "length": 2, "orientation": 'h'},
}

def update_board(board:list, car_dict, car_red) -> list:

    for car_id, car_val in car_dict.items():
        row = car_val.get('row')
        col = car_val.get('col')

        if car_val.get('orientation') == 'h':
            board[row][col] = str(car_id)
            for i in range(car_val.get('length')):
                board[car_val.get('row')][col+i] = str(car_id)

        if car_val.get('orientation') == 'v':
            board[row][col] = str(car_id)
            for k in range(car_val.get('length')):
                board[row+k][col] = str(car_id) 
            
    # Red car
    for car_id, car_val in car_red.items():
        row = car_val.get('row')
        col = car_val.get('col')

        if car_val.get('orientation') == 'h':
            board[row][col] = str(car_id)
            for i in range(car_val.get('length')):
                board[car_val.get('row')][col+i] = str(car_id)

        if car_val.get('orientation') == 'v':
            board[row][col] = str(car_id)
            for k in range(car_val.get('length')):
                board[row+k][col] = str(car_id) 

    return board

class Car():
    def __init__(self, car_id, car_dict ,board):
        self.car_id = car_id
        self.row = car_dict[car_id].get('row')
        self.col = car_dict[car_id].get('col')
        self.len = car_dict[car_id].get('length')
        self.orientation = car_dict[car_id].get('orientation')
        self.board = board

    def move(self, direction):
        board = self.board
        if self.orientation == 'v':
            try:
                if board[(self.row)][self.col + self.len] == '.':
                    print("pos")
            except:
                print("not possible to move")

        if self.orientation == 'h':
            if direction == 'right':
                try:
                    if board[(self.row)][self.col + self.len] == '.':
                        self._col += 1
                    else:
                        print("not possilbe to move: other object")
                except:
                    print("not possible to move")
            if direction == 'left':
                try:
                    if board[(self.row)][self.col-1] == '.':
                        print()
                        self._col =1
                    else:
                        print("not possible to move: other object")
                except:
                    print("not possible to move")

class Board():
    def __init__(self, length, width, cars_dict, red_car):
        self.length = length
        self.width = width
        self.cars = cars_dict
        self.red_car = red_car
        self.init_board = self.create_board()
        self.board = self.add_cars()
    
    def create_board(self):
        board = []
        for row in range(length):
            board.append([])
            for col in range(width):
                board[row].append('.')

        return board

    def add_cars(self):
        
        board_with_cars = self.init_board 
        for car_id, car_val in self.cars.items():
            row = car_val.get('row')
            col = car_val.get('col')

            if car_val.get('orientation') == 'h':
                board_with_cars[row][col] = str(car_id)
                for i in range(car_val.get('length')):
                    board_with_cars[car_val.get('row')][col+i] = str(car_id)

            if car_val.get('orientation') == 'v':
                board_with_cars[row][col] = str(car_id)
                for k in range(car_val.get('length')):
                    board_with_cars[row+k][col] = str(car_id) 
                
        # Red car
        for car_id, car_val in self.red_car.items():
            row = car_val.get('row')
            col = car_val.get('col')

            if car_val.get('orientation') == 'h':
                board_with_cars[row][col] = str(car_id)
                for i in range(car_val.get('length')):
                    board_with_cars[car_val.get('row')][col+i] = str(car_id)

            if car_val.get('orientation') == 'v':
                board_with_cars[row][col] = str(car_id)
                for k in range(car_val.get('length')):
                    board_with_cars[row+k][col] = str(car_id) 
        return board_with_cars

    def output(self):
        for row in self.board:
            print(" ".join(row))

    def possible_moves_horizontal(self):
        possible_moves_hor = []
        # extract moves left
        for i in range(len(self.board)):
            
            array_board = self.board[i]
            num_pos_moves = 0

            for count, value in enumerate(array_board): # value is car id on the board
                if (value is not '.') and (num_pos_moves > 0) and (array_board[count+1] == value) and (array_board[count-1] == '.'):
                    
                    possible_moves_hor.append([value, "left", num_pos_moves])
                    num_pos_moves = 0
                if value is '.': 
                    num_pos_moves = num_pos_moves+1
                if (value is not '.') and (array_board[count-1] != value) and (array_board[count+1] != value):
                    num_pos_moves = 0
        # extract moves rigth
        for i in range(len(self.board)):
            num_pos_moves = 0
            array_board = self.board[i]
            reverse_hor_board = array_board[::-1]

            for count, value in enumerate(reverse_hor_board[:-1]):
                if (value is not '.') and (num_pos_moves > 0) and (reverse_hor_board[count+1] == value) and (reverse_hor_board[count-1] == '.'):
                    possible_moves_hor.append([value, "right", num_pos_moves])
                    num_pos_moves = 0
                if value is '.': 
                    num_pos_moves = num_pos_moves+1
                if (value is not '.') and (reverse_hor_board[count-1] != value) and(reverse_hor_board[count+1] != value):
                    num_pos_moves = 0
        return possible_moves_hor
    
    def execute_stop(self):
        '''
        - stop if the red car is on the right side
        - red car is always on the 2nd line from above (game defintion)
        '''
        #for i in range(len(self.board)):
    
        array_board = self.board[1]
        reverse_hor_board = array_board[::-1]

        if reverse_hor_board[0] == 'R':
            print('Game solved!')
            print('Final Board:')
            return True
        if reverse_hor_board[0] != 'R':
            return False

    def possible_moves_vertical(self):
        possible_moves_ver = []
        # extract moves left
        num_pos_moves = 0
    
        # create list on verticals
        for k in range(len(self.board[0])):
            array_board = []

            for i in range(len(self.board)):
                array_board.append(self.board[i][k])

            for count, value in enumerate(array_board[:-1]): # [:-1] last element irrelevant for move -> list out of range

                if (value is not '.') and (num_pos_moves > 0) and (array_board[count+1] == value) and (array_board[count-1] == '.'):
                    possible_moves_ver.append([value, "up", num_pos_moves])
                    num_pos_moves = 0
                if value is '.': 
                    num_pos_moves = num_pos_moves+1
                if (value is not '.') and (array_board[count-1] != value) and (array_board[count+1] != value):
                    num_pos_moves = 0

        for k in range(len(self.board[0])):
            array_board = []
            num_pos_moves = 0
            # moves down

            for i in range(len(self.board)):
                array_board.append(self.board[i][k])
            reverse_ver_board = array_board[::-1]
            for count, value in enumerate(reverse_ver_board[:-1]):
                if (value is not '.') and (num_pos_moves > 0) and (reverse_ver_board[count+1] == value) and (reverse_ver_board[count-1] == '.'):
                    possible_moves_ver.append([value, "down", num_pos_moves])
                    num_pos_moves = 0
                if value is '.': 
                    num_pos_moves = num_pos_moves+1
                if (value is not '.') and (reverse_ver_board[count-1] != value) and(reverse_ver_board[count+1] != value):
                    num_pos_moves = 0
        return possible_moves_ver


def select_random_move(pos_moves):
    move = random.choice(pos_moves)
    max_move = move[2]
    list_moves = []
    for i in range(max_move):
        list_moves.append(i+1)
    move[2] =random.choice(list_moves)
    return move

def update_car_dict(car_dict, car_red, move):
    car_id = move[0]
    if car_id != "R":
        car_id = int(car_id)

        if move[1] == 'right':
            car_dict[car_id]['col'] = (car_dict[car_id].get('col') + int(move[2]))
        if move[1] == 'left':
            car_dict[car_id]['col'] = (car_dict[car_id].get('col') - int(move[2]))
        if move[1] == 'up':
            car_dict[car_id]['row'] = (car_dict[car_id].get('row') + int(move[2]))
        if move[1] == 'down':
            car_dict[car_id]['row'] = (car_dict[car_id].get('row') - int(move[2]))

    if car_id == 'R':
        if move[1] == 'right':
            car_red[car_id]['col'] = (car_red[car_id].get('col') + int(move[2]))
        if move[1] == 'left':
            car_red[car_id]['col'] = (car_red[car_id].get('col') - int(move[2]))
        if move[1] == 'up':
            car_red[car_id]['row'] = (car_red[car_id].get('row') + int(move[2]))
        if move[1] == 'down':
            car_red[car_id]['row'] = (car_red[car_id].get('row') - int(move[2]))

    return car_dict, car_red


# Red-Car definiton
instance_board = Board(8,8, car_dict, car_red) 

instance_board.output()
pos_moves_hor = instance_board.possible_moves_horizontal()
pos_moves_ver = instance_board.possible_moves_vertical()
pos_moves = pos_moves_hor + pos_moves_ver
# function for random move needs to be extended (only max values are there right now)

move = select_random_move(pos_moves) 
# -> update car dict


    
updated_car_dict = {}
updated_car_red = {}

updated_car_dict, updated_car_red = update_car_dict(car_dict, car_red,move)

exit()

