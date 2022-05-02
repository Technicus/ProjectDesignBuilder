#!/usr/bin/env python3

from pynput.keyboard import Key, Listener
from sys import stdin, stdout


def getpass(prompt = "Password: "):
    import termios, sys
    fd = stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~termios.ECHO          # lflags
    try:
        termios.tcsetattr(fd, termios.TCSADRAIN, new)
        passwd = input(prompt)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return passwd


def getkey():
    import termios, sys
    fd = stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~termios.ECHO          # lflags
    try:
        termios.tcsetattr(fd, termios.TCSADRAIN, new)
        with Listener(on_press=pressed, on_release=released) as detector:
            detector.join()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
        termios.tcflush(fd, termios.TCIFLUSH)


def pressed(key):
    print(f"  Pressed: {key}")
    stdout.flush()


def released(key):
    print(f"  Released: {key}")
    stdout.flush()
    if key == Key.esc:
        # Stop detecting when esc key is pressed
        return False


def cursor(visible = True):
    if visible:
        stdout.write("\033[?25h")
        stdout.flush()
    else:
        stdout.write("\033[?25l")
        stdout.flush()


def test_keypress():
    cursor(False)
    print('\n[ Keypress analysis ]')
    getkey()
    cursor(True)
    print()


def test_hidden_text():
    # Below loop for Detcting keys runs until enter key is pressed
    print(f"[ Hidden input ]")
    text = getpass("  Hidden text: ")
    print(f"\n  Hidden text: {text}\n")


def move_cursor(key):
    #print(f"  key: {key}")
    if key == Key.up:
        stdout.write("\033[1A")
        #print(f"(UP)", end = "")
        stdout.flush()
    if key == Key.down:
        stdout.write("\033[1B")
        #print(f"(DOWN)", end = "")
        stdout.flush()

    if key == Key.left:
        stdout.write("\033[1D")
        #print(f"(UP)", end = "")
        stdout.flush()
    if key == Key.right:
        stdout.write("\033[1C")
        #print(f"(DOWN)", end = "")
        stdout.flush()

    if key == Key.esc:
        # Stop detecting when esc key is pressed
        stdout.flush()
        return False


def test_move_cursor():
    print('\n[ Move cursor ]')
    #cursor(False)

    import termios, sys
    fd = stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~termios.ECHO          # lflags
    try:
        termios.tcsetattr(fd, termios.TCSADRAIN, new)
        #passwd = input(prompt)
        with Listener(on_press=move_cursor) as detector:
            detector.join()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
        termios.tcflush(fd, termios.TCIFLUSH)
    termios.tcflush(fd, termios.TCIFLUSH)
    stdout.flush()
    #cursor(True)
    print()

#test_keypress()
#test_hidden_text()
test_move_cursor()


"""
https://developpaper.com/linux-tips-set-terminal-character-display-color-and-move-cursor-position-in-code/
Escape code 	meaning
Esc[nA 	Move the cursor up n rows, and the number of columns remains unchanged. Move to the top of the terminal and do not move again
Esc[nB 	Move the cursor down n rows, and the number of columns remains unchanged. Move to the bottom of the terminal and do not move again
Esc[nC 	The cursor moves n columns to the right, and the number of rows remains unchanged. Move to the far right of the terminal and do not move again
Esc[nD 	The cursor moves n columns to the left, and the number of rows remains unchanged. Move to the left end of the terminal and do not move again
Esc[nE 	Move the cursor down n rows, and the number of columns changes to the beginning of the row
Esc[nF 	Move the cursor up n rows, and the number of columns changes to the beginning of the row
Esc[Line;ColumnH 	Move the cursor to the specified number of rows and columns. If no value is provided, the default value is 0
Esc[ColumnG 	Move the cursor to the column with the current number of rows unchanged
Esc[s 	Save the current cursor position, and then use ESC [u] to jump to the saved position
Esc[u 	Jump to the cursor position saved by ESC [S]
Esc[?25l 	Hide cursor (lowercase L after 25)
Esc[?25h 	Show cursor
"""
