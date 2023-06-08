#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`console_main` module

:author: Ajgoun Azzedine , Francois Corantin

:date: 2 october 2019

Main module to play the minesweeper's game : console version
"""

import sys
import minesweeper


def main():
    """
    main function for console minesweeper game
    """
    if len(sys.argv) == 4:
        width = int(sys.argv[1])
        height = int(sys.argv[2])
        nbombs = int(sys.argv[3])
    else:
        width = 10
        height = 5
        nbombs = 1
    game = minesweeper.Minesweeper(width, height, nbombs)
    
    ## Board
    
    grid_nb_width=''
    first_line=''
    for n in range(width) :
        grid_nb_width += ('   '+str(n))
        first_line+='+---'
    print(' '+grid_nb_width)
    print(' '+first_line+'+')
    
    value=''
    col =''
    line=''
    for i in range(height) :
        col =''
        line=''
        for m in range(width) :
            value= game.get_cell(m,i)
            col+= '| '+str(value)+' '
        for n in range(width) :
            line+='+---'
        print(str(i)+col+'|')
        print(' '+line+'+')
    
    ## game, récursion
    
    if game.get_state == minesweeper.GameState.winning  :
        print("You win!")        
    elif game.get_state == minesweeper.GameState.losing :
        print("You lose!")
    else :
        x=input('x position')
        y=input('y position')
        C=input('(R)eveal,(S)et,(U)nset')
        print("Your play x,y,C (C=(R)eveal,(S)et,(U)nset):" + x + ',' + y + ',' + C + ',')
        if C == 'R' :
            game.reveal_all_cells_from(int(x),int(y))
        elif C == 'S' :
            cel = game.get_cell(int(x),int(y))
            cel.set_hypothetic()
        elif C == 'U' :
            cel = game.get_cell(int(x),int(y))
            cel.unset_hypothetic()
        return main()
    
    
if __name__ == '__main__':
    main()
    