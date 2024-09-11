import curses
from curses import wrapper
import time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    BLUE_AND_BLACK = curses.color_pair(1)
    RED_AND_BLACK = curses.color_pair(2)

    counter_win = curses.newwin(1, 20, 10, 10)
    stdscr.addstr("hello world!")
    stdscr.refresh()

    for i in range(100):
        counter_win.clear()
        color = BLUE_AND_BLACK

        if i % 2 == 0:
            color = RED_AND_BLACK

        counter_win.addstr(f"Count: {i}", color)
        counter_win.refresh()
        time.sleep(0.1)

    stdscr.getch()

wrapper(main)