import curses
from curses import wrapper

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    MAGENTA_AND_WHITE = curses.color_pair(2)

    stdscr.clear()
    stdscr.addstr(25, 40, "hello world", BLUE_AND_YELLOW | curses.A_UNDERLINE)
    stdscr.addstr(15, 60, "goodbye world", MAGENTA_AND_WHITE | curses.A_REVERSE)
    stdscr.refresh()
    stdscr.getch()

wrapper(main)