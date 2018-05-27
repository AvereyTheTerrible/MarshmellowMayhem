# -*- coding: utf-8 -*-
"""
Created on Sun May 27 10:28:42 2018
Game Board
@author: ytomk
"""

from collections import namedtuple


Cube = namedtuple('cube', 'x y z')
Axial = namedtuple('axial', 'q r')

class HexBoard:
    def __init__(self, dimension):
        print('HEX board dimension: {}'.format(dimension))
        self.dimension = dimension
        
    def __repr__(self):
        return 'HEX board {}'.format(self.dimension)

    @staticmethod
    def cube_to_axial(cube):
        q = cube.x
        r = cube.z
        return Axial(q, r)
    
    @staticmethod
    def axial_to_cube(axial):
        x = axial.q
        z = axial.r
        y = -x-z
        return Cube(x, y, z)
        
def main():
    hex1 = HexBoard((2,10))
    print(hex1)
    print(HexBoard.cube_to_axial(Cube(1, 2, -3)))
    print(HexBoard.axial_to_cube(Axial(1, 2)))
    
if __name__ == '__main__':
    main()