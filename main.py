
#import numpy as np






class car():
    '''
    Attributes:
    - length
    - direction
    - start_coordinates
    - actual coordinates
    -- need two coordinates? 

    
    Method:
    move -> dependent on direction, start_coordinates
    - update actual coordinates

    '''



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
width = 8

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

    def extract_possible_mvoes(self):
        possible_moves = []
        # extract moves left
        for i in range(len(self.board)):
            
            array_board = self.board[i]
            amount_moves = 0

            for count, value in enumerate(array_board): # value is car id on the board
                if (value is not '.') and (amount_moves > 0) and (array_board[count+1] == value) and (array_board[count-1] == '.'):
                    
                    possible_moves.append([value, "left", amount_moves])
                    amount_moves = 0
                if value is '.': 
                    amount_moves = amount_moves+1
                if (value is not '.') and (array_board[count-1] != value) and (array_board[count+1] != value):
                    amount_moves = 0
        # extract moves rigth
        for i in range(len(self.board)):

            amount_moves = 0
            array_board = self.board[i]
            reverse_board = array_board[::-1]

            for count, value in enumerate(reverse_board[:-1]):
                if (value is not '.') and (amount_moves > 0) and (reverse_board[count+1] == value) and (reverse_board[count-1] == '.'):
                    possible_moves.append([value, "right", amount_moves])
                    amount_moves = 0
                if value is '.': 
                    amount_moves = amount_moves+1
                if (value is not '.') and (reverse_board[count-1] != value) and(reverse_board[count+1] != value):
                    amount_moves = 0
        return possible_moves



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


# Red-Car definiton
instance_board = Board(8,8, car_dict, car_red) 

instance_board.output()
possible_moves = [] # a dict for pos moves with key-value pair: car-id - move

possible_moves = instance_board.extract_possible_mvoes()
print(possible_moves)
exit()
#print(instance_board.board)

for car_id, _ in car_dict.items():
    if car_id ==car_id:
        #print(car_dict[car_id].get('col'))

        # extract possible moves:


        car = Car(car_id, car_dict, instance_board.board)
        

 
        car.move(direction='left')


        #exit()
'''            print(car_val)
            car_val.get('row')
            car_val.get('col')
            car_val.get('length')
            car_val.get('orientation')

            car_test = Car(car_val.get('row'), car_val.get('col'), car_val.get('length'), car_val.get('orientation'), instance_board.board )
            car_test.move(direction='left')


            print(car_val)
            print('########################')
'''

# pseudo code:
# - Cars move method -> dep: Board
# - 
