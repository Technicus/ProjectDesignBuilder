# ProjectDesignBuilder
 This is an attempt to design a graphical application with the Tkinter Pthon library for a custom CadQuery interface.  I intend to develop it as a utility for creating technical drawings from models.  The drawings can be exported as SVG, PNG, DXF, or perhaps other formats.

 So far it consists of a root window, a menubar, a tool bar, a status bar,
 a mode bar, and a working frame, a background picture, and a toolbar icon.

## Guidance for development
I have been asking for guidance in chat groups on Discord Python, Discord Tkinter, and Discord CadQuery.  I been reading many resources, and reviewing numerous tutorials.

## Tkinter
[Tkinter](https://docs.python.org/3/library/tkinter.html) is what I have decided to use because for this project because . . . I am not currently able to articulate why, and do not want to put any more effort in attempting to learn a different interface toolkit, regardless of how easy it might be.
Perhaps I might try a different one after I actually make something with this one.

## CadQuery
[CadQuery](https://cadquery.readthedocs.io/en/latest/intro.html#id1) is a very interesting library, and a significant reason for why I am creating [ProjectDesignBuilder](https://github.com/Technicus/ProjectDesignBuilder).

## Current Status
I am attempting to understand how methods can be added to classes while the program is being interpreted.
This project I am working on is a sandbox for me to learn with.
The class 'Project_Root' I am attempting to add methods to is for drawing a window with thinter.
I am creating a status bar, which is a frame that has labels placed in it.
The information, configuration, and other pertinant reference data that define the labels are in a dictionary defined as `event_callback_assignmet` in the module `./status/status_assignment.py`.
In the `event_callback_assignmet` dictionary there are references to functions which are defined in the module `./status/status_calls.py`.
My intent is to add that functions as methods in the `Project_Root` class.
The reason I have adopted this approach is so that I can make changes to the dictionary file, and add functions to the function file, and import them rather them having them in the root window class.
My reasoning for this approach is to manipulat the window elements with different configurations and make it extensible.
I am a novice, not a student, doing this as a hobby for my own interest, and am not employed as a programmer, nor do I have decades of experience programming sophisticated interfaces.
I do not know best practices, optimal methods, nor am I interested in exestential philosophical discussions about why I am trying to program this way or why I am even doing it.
This is really my first time actually trying to write a desktop application.




