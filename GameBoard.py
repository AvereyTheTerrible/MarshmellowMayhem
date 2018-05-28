# -*- coding: utf-8 -*-
"""
Created on Sun May 27 10:28:42 2018
Game Board
@author: ytomk
"""

from collections import namedtuple

'''
    Cube coordinates:
        
            -z
           /\
          /  \
         /    \
        /      \  +x
    +y |\      /| 
       | \    / |
       |  \  /  |
       |   \/   |
    -x  \   |   / -y
         \  |  /
          \ | /
           \|/
           +z
    
    with constraints x + y + z = 0
    
'''

class CoordCube:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        return 'cube({}, {}, {})'.format(self.x, self.y, self.z)
        
    def __add__(self, other):
        return CoordCube(self.x + other.x,
                         self.y + other.y,
                         self.z + other.z)
    def __sub__(self, other):
        return CoordCube(self.x - other.x,
                         self.y - other.y,
                         self.z - other.z)
    def to_axial(self):
        q = self.x
        r = self.z
        return CoordAxial(q, r)
    
class CoordAxial:
    def __init__(self, q, r):
        self.q = q
        self.r = r
        
    def __repr__(self):
        return 'axial({}, {})'.format(self.q, self.r)
    
    def to_cube(self):
        return CoordCube(self.q, -self.q - self.r, self.r)


        
class HexBoard:
    cube_dirs = [CoordCube(+1, -1, 0),
                       CoordCube(+1, 0, -1),
                       CoordCube(0, +1, -1),
                       CoordCube(-1, +1, 0),
                       CoordCube(-1, 0, +1),
                       CoordCube(0, -1, +1)]

    def __init__(self, dimension):
        print('HEX board dimension: {}'.format(dimension))
        self.dimension = dimension
        
    def __repr__(self):
        return 'HEX board {}'.format(self.dimension)

    @staticmethod
    def cube_to_axial(cube):
        q = cube.x
        r = cube.z
        return CoordAxial(q, r)
    
    @staticmethod
    def axial_to_cube(axial):
        x = axial.q
        z = axial.r
        y = -x-z
        return CoordCube(x, y, z)
    
    @staticmethod
    def neighbor(cube, direction):
        return cube + HexBoard.cube_dirs[direction % len(HexBoard.cube_dirs)]

    
def main():
    hex1 = HexBoard((2,10))
    print(hex1)
    c1 = CoordCube(1, 2, -3)
    c2 = CoordCube(1, -1, 0)
    print('{} - {} = {}'.format(c1, c2, c1 - c2))
    a1 = CoordAxial(1, 1)
    print('{} <=> {}'.format(c1, c1.to_axial()))
    print('{} <=> {}'.format(a1, a1.to_cube()))
    print('neighbors of {}'.format(c1))
    for i in range(6):
        print('\t{} neighbor {}'.format(i, HexBoard.neighbor(c1, i)))
    
if __name__ == '__main__':
    main()