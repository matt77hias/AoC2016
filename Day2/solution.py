###################################################################################################################################################################################
## Solution
################################################################################################################################################################################### 
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def get_fname(name, path=__location__):
    return os.path.join(path, name)
    
def calc_keys(fname):
    current_position = [0,0]
    with open(fname, 'r') as fstream:
        for line in fstream:
            key, current_position = calc_key(data=line, current_position=current_position)
            
def calc_key(data, current_position=[0,0]):
    keypad = ((7,8,9),(4,5,6),(1,2,3))
    for movement in data:
        if movement is 'R':
            current_position[0] += 1
        elif movement is 'L':
            current_position[0] -= 1
        elif movement is 'U':
            current_position[1] += 1
        elif movement is 'D':
            current_position[1] -= 1
        
        current_position[0] = clamp(current_position[0], -1, 1)     
        current_position[1] = clamp(current_position[1], -1, 1)
    
    key = keypad[1 + current_position[1]][1 + current_position[0]]
    print('Position: ' + str(current_position))
    print('Key: ' + str(key))
    
    return key, current_position
        
def clamp(x, low, high):
    return low if (x < low) else (high if (x > high) else x)
    
###################################################################################################################################################################################
## Tests
###################################################################################################################################################################################
if __name__ == "__main__":
    calc_keys(fname=get_fname('input.txt'))
      
def test_suite():
    current_position = [0,0]
    key, current_position = calc_key('ULL',   current_position=current_position)
    key, current_position = calc_key('RRDDD', current_position=current_position)
    key, current_position = calc_key('LURDL', current_position=current_position)
    key, current_position = calc_key('UUUUD', current_position=current_position)
