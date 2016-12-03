###################################################################################################################################################################################
## Solution
################################################################################################################################################################################### 
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def get_fname(name, path=__location__):
    return os.path.join(path, name)
      
def extract_data_from_file(fname):
    data = ''
    file = open(fname, 'r')
    try:
	data = file.read()
    finally:
	file.close()
    return data
	
def extract_movement_formats(data):
    return [movement_format.strip() for movement_format in data.split(', ')]

def extract_turn(movement_format):
    return 1 if movement_format[0] == 'R' else -1

def extract_steps(movement_format):
    return int(movement_format[1:])

def extract_movement(movement_format):
    return extract_turn(movement_format=movement_format), extract_steps(movement_format=movement_format)

def extract_movements(data):
    return [extract_movement(movement_format=movement_format) for movement_format in extract_movement_formats(data)]
    
def calc_blocks_from_file(fname):
    return calc_blocks(data=extract_data_from_file(fname=fname))

def calc_blocks(data):
    current_orientation = 0
    current_position = [0,0] # y, x
    for (turn, steps) in extract_movements(data=data):
        current_orientation = (current_orientation + turn) % 4
        axis = current_orientation % 2
        if (current_orientation < 2):
            current_position[axis] += steps
        else:
            current_position[axis] -= steps
    
    return manhattan_distance(current_position), current_position[::-1]
            
def manhattan_distance(p1, p2=[0,0]):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
###################################################################################################################################################################################
## Tests
###################################################################################################################################################################################
if __name__ == "__main__":
    distance, position = calc_blocks_from_file(fname=get_fname('input.txt'))
    print('Position: ' + str(position))
    print('Distance: ' + str(distance))
    
def test_suite():
    test(5, 'R2, L3')
    test(5, 'L2, R3')
    test(2, 'R2, R2, R2')
    test(12, 'R5, L5, R5, R3')
    test(0, 'L5, L0, L5, L0')
    test(0, 'R5, R0, R5, R0')
    
def test(exact, data):
    print('Solution: ' + str(exact) + '\tCalculated solution: '+ str(calc_blocks(data=data)[0]))