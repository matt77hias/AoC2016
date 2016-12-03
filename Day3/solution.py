###################################################################################################################################################################################
## Solution
################################################################################################################################################################################### 
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def get_fname(name, path=__location__):
    return os.path.join(path, name)
    
def load_data(fname):
    with open(fname, 'r') as fstream:
        return [map(int, line.split()) for line in fstream]
    
def calc_validness_triangles(data):
    return len([triangle for triangle in data if is_valid_triangle(*triangle)])
    
def is_valid_triangle(a, b, c):
    return ((a + b) > c) and ((b + c) > a) and ((a + c) > b)
    
def calc_validness_triangles2(data):
    nb_valid = 0
    for i in range(0, len(data), 3):
        for j in range(len(data[0])):
            nb_valid += is_valid_triangle(data[i][j], data[i+1][j], data[i+2][j])
    return nb_valid
    
###################################################################################################################################################################################
## Tests
###################################################################################################################################################################################
if __name__ == "__main__":
    data = load_data(fname=get_fname('input.txt'))
    print('Valid Triangles: ' + str(calc_validness_triangles(data=data)))
    print('Valid Triangles: ' + str(calc_validness_triangles2(data=data)))
      
def test_suite():
    print('Solution: False\tCalculated solution: ' + str(is_valid_triangle(5, 10, 25)))
    print('Solution: True\tCalculated solution: ' + str(is_valid_triangle(3, 4, 5)))