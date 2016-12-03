###################################################################################################################################################################################
## Solution
################################################################################################################################################################################### 
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def get_fname(name, path=__location__):
    return os.path.join(path, name)
    
def calc_validness_triangles(fname):
    nb_valid = 0
    with open(fname, 'r') as fstream:
        for line in fstream: 
            args = map(int, line.split())
            nb_valid += calc_validness_triangle(*args)
            
    
    
    return nb_valid
    
def calc_validness_triangle(a, b, c):
    return ((a + b) > c) and ((b + c) > a) and ((a + c) > b)
    
###################################################################################################################################################################################
## Tests
###################################################################################################################################################################################
if __name__ == "__main__":
    print('Valid Triangles: ' + str(calc_validness_triangles(fname=get_fname('input.txt'))))
      
def test_suite():
    print('Solution: False\tCalculated solution: ' + str(calc_validness_triangle(5, 10, 25)))
    print('Solution: True\tCalculated solution: ' + str(calc_validness_triangle(3, 4, 5)))