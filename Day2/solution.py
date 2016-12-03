###################################################################################################################################################################################
## Solution
################################################################################################################################################################################### 
from copy import copy
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def get_fname(name, path=__location__):
    return os.path.join(path, name)
    
def calc_keys(fname, keypad, current_position):
    keycode = ''
    with open(fname, 'r') as fstream:
        for line in fstream:
            key, current_position = calc_key(data=line, keypad=keypad, current_position=current_position)
            keycode += key
    return keycode
                    
def calc_key(data, keypad, current_position):
    for movement in data:
        old_position = copy(current_position)
        
        if movement is 'R':
            current_position[1] += 1
        elif movement is 'L':
            current_position[1] -= 1
        elif movement is 'U':
            current_position[0] += 1
        elif movement is 'D':
            current_position[0] -= 1
        
        if (current_position[0] < 0 or current_position[0] >= len(keypad) or \
            current_position[1] < 0 or current_position[1] >= len(keypad[0]) or \
            keypad[current_position[0]][current_position[1]] is '_'):
                current_position = copy(old_position)

    return keypad[current_position[0]][current_position[1]], current_position
    
###################################################################################################################################################################################
## Tests
###################################################################################################################################################################################
def test_suite():
    current_position = [1,1]
    keypad = (('7','8','9'),('4','5','6'),('1','2','3'))
    key, current_position = calc_key('ULL',   keypad=keypad, current_position=current_position)
    print('Key: ' + str(key))
    key, current_position = calc_key('RRDDD', keypad=keypad, current_position=current_position)
    print('Key: ' + str(key))
    key, current_position = calc_key('LURDL', keypad=keypad, current_position=current_position)
    print('Key: ' + str(key))
    key, current_position = calc_key('UUUUD', keypad=keypad, current_position=current_position)
    print('Key: ' + str(key))
    
    current_position = [2,0]
    keypad = (('_', '_', 'D', '_', '_'),
              ('_', 'A', 'B', 'C', '_'),
              ('5', '6', '7', '8', '9'),
              ('_', '2', '3', '4', '_'),
              ('_', '_', '1', '_', '_'))
    key, current_position = calc_key('ULL',   keypad=keypad, current_position=current_position)
    print('Key: ' + str(key))
    key, current_position = calc_key('RRDDD', keypad=keypad, current_position=current_position)
    print('Key: ' + str(key))
    key, current_position = calc_key('LURDL', keypad=keypad, current_position=current_position)
    print('Key: ' + str(key))
    key, current_position = calc_key('UUUUD', keypad=keypad, current_position=current_position)
    print('Key: ' + str(key))

if __name__ == "__main__":
    current_position = [1,1]
    keypad = (('7','8','9'),('4','5','6'),('1','2','3'))
    keycode = calc_keys(fname=get_fname('input.txt'), keypad=keypad, current_position=current_position)
    print('Keycode: ' + str(keycode))

    current_position = [2,0]
    keypad = (('_', '_', 'D', '_', '_'),
              ('_', 'A', 'B', 'C', '_'),
              ('5', '6', '7', '8', '9'),
              ('_', '2', '3', '4', '_'),
              ('_', '_', '1', '_', '_'))
    keycode = calc_keys(fname=get_fname('input.txt'), keypad=keypad, current_position=current_position)
    print('Keycode: ' + str(keycode))