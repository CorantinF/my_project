#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`minesweeper` module

:author: Ajgoun Azzedine , Francois Corantin

:date: 2 october 2019

This module provides functions and a class for minesweeper's game's management.

"""

import random
from enum import Enum
from cell import Cell

################################################
# Type declaration
################################################

class GameState(Enum):
    """
    A class to define an enumerated type with three values :

    * ``winning``
    * ``losing``
    * ``unfinished``

    for the three state of minesweeper game.
    """
    winning = 1
    losing = 2
    unfinished = 3


##############################################
# Function for game's setup and management
##############################################


def neighborhood(x, y, width, height):
    """
    :param x: x-coordinate of a cell
    :type x: int
    :param y: y-coordinate of a cell
    :type y: int
    :param height: height of the grid
    :type height: int
    :param width: width of the grid
    :type width: int
    :return: the list of coordinates of the neighbors of position (x,y) in a
             grid of size width*height
    :rtype: list of tuple
    :UC: 0 <= x < width and 0 <= y < height
    :Examples:

    >>> neighborhood(3, 3, 10, 10)
    [(2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)]
    >>> neighborhood(0, 3, 10, 10)
    [(0, 2), (0, 4), (1, 2), (1, 3), (1, 4)]
    >>> neighborhood(0, 0, 10, 10)
    [(0, 1), (1, 0), (1, 1)]
    >>> neighborhood(9, 9, 10, 10)
    [(8, 8), (8, 9), (9, 8)]
    >>> neighborhood(3, 9, 10, 10)
    [(2, 8), (2, 9), (3, 8), (4, 8), (4, 9)]
    """
    liste = [(x-1,y-1), (x-1,y), (x-1,y+1), (x,y-1), (x,y+1), (x+1,y-1), (x+1,y), (x+1,y+1)]
    result = []
    for tuple in liste :
        if not (tuple[0] >= width or tuple[1] >= height or tuple[0] < 0 or tuple[1] < 0 ):
            result.append(tuple)
    return result

class Minesweeper():
    """
    >>> game = Minesweeper(20, 10, 4)
    >>> game.get_width()
    20
    >>> game.get_height()
    10
    >>> game.get_nbombs()
    4
    >>> game.get_state() == GameState.unfinished 
    True
    >>> cel = game.get_cell(1, 2)
    >>> cel.is_revealed()
    False
    >>> 
    """

    def __init__(self, width=30, height=20, nbombs=99):
        """
        build a minesweeper grid of size width*height cells
        with nbombs bombs randomly placed.  

        :param width:[optional] horizontal size of game (default = 30)
        :type width: int
        :param height: [optional] vertical size of game (default = 20)
        :type height: int
        :param nbombs: [optional] number of bombs (default = 99)
        :type nbombs: int
        :return: a fresh grid of  width*height cells with nbombs bombs randomly placed.
        :rtype: Minesweeper
        :UC: width and height must be positive integers, and
             nbombs <= width * height
        :Example:

        >>> game = Minesweeper(20, 10, 4)
        >>> game.get_width()
        20
        >>> game.get_height()
        10
        >>> game.get_nbombs()
        4
        >>> game.get_state() == GameState.unfinished 
        True
        """
        self.__width = width
        self.__height = height
        self.__nbombs = nbombs
        self.__grid = {}
        self.__rbombs = set()
        
        # /!\ créer la grille 
        for line in range(width):
            for column in range(height):
                self.__grid[(line,column)] = Cell()
        
        # /!\ Creer les bombes = choisir aléatoirement les cell qui sont des bombes
        while len(self.__rbombs) != nbombs :
            x = random.randint(0,width-1)
            y = random.randint(0,height-1)
            cel = self.get_cell(x,y).set_bomb()
            self.__rbombs.add((x,y))
 
        # /!\ mettre à jour les "nb bombes dans voisinage"
        for rbombs in self.__rbombs :
            for voisins in neighborhood(rbombs[0],rbombs[1],width,height) :
                cel = self.get_cell(voisins[0],voisins[1])
                cel.incr_number_of_bombs_in_neighborhood()
        
    def get_height(self):
        """
        :return: height of the grid in self
        :rtype: int
        :UC: none
        """
        return self.__height

    def get_width(self):
        """
        :return: width of the grid in game
        :rtype: int
        :UC: none
        """
        return self.__width    
    
    def get_nbombs(self):
        """
        :return: number of bombs in game
        :rtype: int
        :UC: none
        """
        return self.__nbombs

    def get_cell(self, x, y):
        """
        :param x: x-coordinate of a cell
        :type x: int
        :param y: y-coordinate of a cell
        :type y: int
        :return: the cell of coordinates (x,y) in the game's grid
        :type: cell
        :UC: 0 <= x < width of game and O <= y < height of game
        """
        return self.__grid[(x,y)]

    def get_state(self):
        """
        :return: the state of the game (winning, losing or unfinished)
        :rtype: GameState
        :UC: none
        """
        cpt = 0
        for coords in self.__grid :
            cel = self.get_cell(coords[0],coords[1])
            if cel.is_revealed() == True :
                cpt += 1
            elif cel.is_revealed() == True and cel.is_bomb() == True :
                return GameState(2)
        if cpt == len(self.__grid) - len(self.__rbombs) :
            return GameState(1)
        else:
            return GameState(3)
        
    def reveal_all_cells_from(self, x, y):
        """
        :param x: x-coordinate
        :param y: y-coordinate
        :return: none
        :side effect: reveal all cells of game from the initial cell (x,y).
        :UC: 0 <= x < width of game and O <= y < height of game
        """
        cel=self.get_cell(x,y)
        if cel.is_revealed() == True :
            return None
        elif cel.is_bomb() == False and cel.number_of_bombs_in_neighborhood() != 0 :
            cel.reveal()
        elif cel.is_bomb() == True :
            for cells in self.__grid:
                cel=self.get_cell(cells[0],cells[1])
                cel.reveal()
        else:
            cel.reveal()
            for coords in neighborhood(x,y,self.get_width(),self.get_height()):
                self.reveal_all_cells_from(coords[0],coords[1])
        
         
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)


