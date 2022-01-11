







class Car():
    def __init__(self, row, col, len, orientation, board):
        self.row = row
        self.col = col
        self.len = len
        self.orientation = orientation
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
                        print("calleee")
                        self._col =1
                    else:
                        print("not possible to move: other object")
                except:
                    print("not possible to move")


# Add:
# Board-logic:
# - Cars not over each other

# Main:
# - create board
# - create all cars -> dict with definitions
# - place cars on it
# - calculate every posible state from the current one



# Board:
length = 8
width = 8

# Car-definitions
car_dict = {
    1: {"row": 1, "col": 3, "length": 3, "orientation": 'v'},
    2: {"row": 4, "col": 5, "length": 2, "orientation": 'h'},
    3: {"row": 7, "col": 3, "length": 4, "orientation": 'h'},
    4: {"row": 0, "col": 3, "length": 4, "orientation": 'h'},
    5: {"row": 1, "col": 4, "length": 4, "orientation": 'v'},
    6: {"row": 5, "col": 2, "length": 3, "orientation": 'h'},
    7: {"row": 6, "col": 2, "length": 5, "orientation": 'h'},
    8: {"row": 3, "col": 0, "length": 5, "orientation": 'v'},

}

car_red = {
    'R': {"row": 1, "col": 1, "length": 2, "orientation": 'h'},
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


# Red-Car definiton
instance_board = Board(8,8, car_dict, car_red) 

instance_board.output()

#print(instance_board.board)
for car_id, car_val in car_dict.items():
    if car_id ==6:
            print(car_val)
            car_val.get('row')
            car_val.get('col')
            car_val.get('length')
            car_val.get('orientation')

            car_test = Car(car_val.get('row'), car_val.get('col'), car_val.get('length'), car_val.get('orientation'), instance_board.board )
            car_test.move(direction='left')
            print(car_val)
            print('########################')

