import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(25, 40, "hello world", curses.A_UNDERLINE)
    stdscr.addstr(15, 60, "goodbye world")
    stdscr.addstr(15, 55, "overwritten")
    stdscr.refresh()
    stdscr.getch()

wrapper(main)