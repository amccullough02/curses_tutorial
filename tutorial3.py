import curses
from curses import wrapper
import time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    BLUE_AND_BLACK = curses.color_pair(1)
    RED_AND_BLACK = curses.color_pair(2)

    pad = curses.newpad(100, 100)
    stdscr.refresh()

    for i in range(100):
        for j in range(26):
            char = chr(67 + j)
            pad.addstr(char, BLUE_AND_BLACK)

    # pad_y1, pad_x1, screen_x, screen_y, pad_y2, pad_x2
    pad.refresh(0, 0, 5, 10, 25, 50)
    stdscr.getch()

wrapper(main)