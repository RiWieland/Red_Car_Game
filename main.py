







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
# - calculate every posible state from the current one



#Create player board
def create_board(length=int, weigth=int) -> list:

    player_board = []

    for player_row in range(length):
        player_board.append([])
        for player_col in range(width):
            player_board[player_row].append('.')

    return player_board

#Print player board
def print_board(player_board: list):
    for player_row in player_board:
        print(" ".join(player_row))
    


'''
def player_place_ships(player_board, ships):
      for i, j in ships.items():
    ship_not_place = true
    while ship_not_placed :
      ori = input('Enter orientation, v or h: ')
      x = int(input('Enter row: '))
      y = int(input('Enter col: '))
      place = x,y
      placement = player_board[x][y]
      if ori == 'v' and placement == '.':
        for k in range(j):
          player_board[x][y] = i 
          player_board[x+k][y] = i
        ship_not_place = false 
      elif ori == 'h' and placement == '.':
        player_board[x][y] = i 
        player_board[x][y+k] = i 
        ship_not_place = false 
      elif ori != 'v'  or 'h' and placement != '.':
        print('Invalid choice, please try again.')
'''

# Board:
length = 8
width = 8

# Car-definitions
car_dict = {
    1: {"x": 1, "y": 3, "length": 3, "orientation": 'v'},
    2: {"x": 4, "y": 5, "length": 2, "orientation": 'h'},
    3: {"x": 7, "y": 3, "length": 4, "orientation": 'h'},
    4: {"x": 0, "y": 3, "length": 4, "orientation": 'h'},
    5: {"x": 1, "y": 4, "length": 4, "orientation": 'v'},
    6: {"x": 5, "y": 2, "length": 3, "orientation": 'h'},
    7: {"x": 6, "y": 2, "length": 5, "orientation": 'h'},
    8: {"x": 3, "y": 0, "length": 5, "orientation": 'v'},

}

car_red = {
    'R': {"x": 1, "y": 1, "length": 2, "orientation": 'h'},
}


def update_board(board:list, car_dict, car_red) -> list:

    for car_id, car_val in car_dict.items():
        x = car_val.get('x')
        y = car_val.get('y')

        if car_val.get('orientation') == 'h':
            board[x][y] = str(car_id)
            for i in range(car_val.get('length')):
                board[car_val.get('x')][y+i] = str(car_id)

        if car_val.get('orientation') == 'v':
            board[x][y] = str(car_id)
            for k in range(car_val.get('length')):
                board[x+k][y] = str(car_id) 
            
    # Red car
    for car_id, car_val in car_red.items():
        x = car_val.get('x')
        y = car_val.get('y')

        if car_val.get('orientation') == 'h':
            board[x][y] = str(car_id)
            for i in range(car_val.get('length')):
                board[car_val.get('x')][y+i] = str(car_id)

        if car_val.get('orientation') == 'v':
            board[x][y] = str(car_id)
            for k in range(car_val.get('length')):
                board[x+k][y] = str(car_id) 

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
            x = car_val.get('x')
            y = car_val.get('y')


            if car_val.get('orientation') == 'h':
                board_with_cars[x][y] = str(car_id)
                for i in range(car_val.get('length')):
                    board_with_cars[car_val.get('x')][y+i] = str(car_id)

            if car_val.get('orientation') == 'v':
                board_with_cars[x][y] = str(car_id)
                for k in range(car_val.get('length')):
                    board_with_cars[x+k][y] = str(car_id) 
                
        # Red car
        for car_id, car_val in self.red_car.items():
            x = car_val.get('x')
            y = car_val.get('y')

            if car_val.get('orientation') == 'h':
                board_with_cars[x][y] = str(car_id)
                for i in range(car_val.get('length')):
                    board_with_cars[car_val.get('x')][y+i] = str(car_id)

            if car_val.get('orientation') == 'v':
                board_with_cars[x][y] = str(car_id)
                for k in range(car_val.get('length')):
                    board_with_cars[x+k][y] = str(car_id) 

        return board_with_cars
        


    def output(self):
        for row in self.board:
            print(" ".join(row))



# Red-Car definiton
instance_board = Board(8,8, car_dict, car_red) 
test = instance_board.create_board()

instance_board.output()

