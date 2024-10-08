import curses
from curses import wrapper
import time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    BLUE_AND_BLACK = curses.color_pair(1)
    RED_AND_BLACK = curses.color_pair(2)

    for i in range(100):
        stdscr.clear()
        color = BLUE_AND_BLACK

        if i % 2 == 0:
            color = RED_AND_BLACK
        stdscr.addstr(f"Count: {i}", color)
        stdscr.refresh()
        time.sleep(0.1)
    stdscr.getch()

wrapper(main)