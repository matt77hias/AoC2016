###################################################################################################################################################################################
## Solution
################################################################################################################################################################################### 
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def get_fname(name, path=__location__):
    return os.path.join(path, name)
    
def calc_validness_from_file(fname):
    with open(fname, 'r') as fstream:
        return reduce(lambda acc, line: acc + calc_validness(data=line.rstrip('\n')), fstream, 0)
    
def calc_validness(data):
    cst, sector_id, check_sum = extract_components(data)
    correct_checksum = extract_correct_checksum(cst)
    if (check_sum == correct_checksum): 
        return sector_id
    else:
        return 0
    
def extract_correct_checksum(cst):
    return reduce(lambda acc, i: acc + cst[i][1], range(5), '')
    
# O(N) time complexity   
def extract_components(data):
    cst = get_char_sum_table()
    sector_id = check_sum = ''
    parts_finished = 0
    for c in reversed(data):
        
        if c is '[':
            parts_finished = 1
            continue
        if c is '-' or c is ']':
            if parts_finished == 1:
                parts_finished = 2
            continue
             
        if parts_finished == 0:
            check_sum = c + check_sum
        elif parts_finished == 1:
            sector_id = c + sector_id
        else:
            cst[char_to_index(c)][0] += 1
            
    return sorted(cst, cmp=cmp_char_sum, reverse=True), int(sector_id), check_sum
    
from string import ascii_lowercase
def get_char_sum_table():
    return map(list, zip([0] * 26, ascii_lowercase))
        
def cmp_char_sum(cs1, cs2):
    if cs1[0] < cs2[0]:
        return -1
    elif  cs1[0] == cs2[0]:
        return cs1[1] < cs2[1]
    else:
        return 1
        
def char_to_index(c):
    return ord(c) - 97
    
###################################################################################################################################################################################
## Tests
###################################################################################################################################################################################
if __name__ == "__main__":
    fname = get_fname('input.txt')
    print('Valid Rooms: ' + str(calc_validness_from_file(fname=fname)))
      
def test_suite():
    print('Solution: 123\tCalculated solution: ' + str(calc_validness('aaaaa-bbb-z-y-x-123[abxyz]')))
    print('Solution: 987\tCalculated solution: ' + str(calc_validness('a-b-c-d-e-f-g-h-987[abcde]')))
    print('Solution: 404\tCalculated solution: ' + str(calc_validness('not-a-real-room-404[oarel]')))
    print('Solution: 0\tCalculated solution: ' + str(calc_validness('totally-real-room-200[decoy]')))