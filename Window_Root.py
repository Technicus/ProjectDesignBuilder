
import tkinter as tk
import sys
from tkinter import PhotoImage, Menu, ttk
from PIL import ImageTk, Image
from configuration.status import reports
from configuration.tools import *
from configuration.menus import *
from configuration.modes import *

class Root(tk.Tk):
    def __init__(self, title, size):
        # main setup
        super().__init__()
        self.title(title)
        self.photo = PhotoImage(file = './image/Screen_check.png')
        self.wm_iconphoto(True, self.photo)
        self.geometry(f'{size[0]}x{size[1]}')
        # self.attributes('-zoomed', True)
        #Make the window jump above all
        self.attributes('-topmost',True)
        self.config(menu = MenuBar(self))
        self.style = ttk.Style(self)
        self.style.configure('background', background = 'red')
        self.root_frame = RootFrame(self)
        self.bind('<Motion>',self.callback)
        self.mainloop()

    def callback(self, value):
        x= value.x
        y= value.y
        # print("self: {}".format(self))
        print("Event: {}".format(value))
        print("Pointer is currently at %d, %d" %(x,y))

        print('\nself.root_frame.status_panel:')
        print(dir(self.root_frame.status_panel))
        print('\nself.root_frame.status_panel.children:')
        print(dir(self.root_frame.status_panel.children))
        print('\nself.root_frame.status_panel.__dict__:')
        print(dir(self.root_frame.status_panel.__dict__))
        print('\nself.root_frame.status_panel.__dir__:')
        print(dir(self.root_frame.status_panel.__dir__))
        print('\nself.root_frame.status_panel.__subclasshook__:')
        print(dir(self.root_frame.status_panel.__subclasshook__))
        print('\nself.root_frame.status_panel.__subclasshook__.__name__:')
        print(dir(self.root_frame.status_panel.__subclasshook__.__name__))

        self.root_frame.status_panel.mouse_position.setText("%d, %d" %(x,y))

class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.create_menubar_(menus)

    def create_menubar_(self, menus):
        self.menubar = tk.Menu(self)
        for menu_option, menu_operations in menus.items():
            setattr(self, menu_option, menu_operations)
            self.menu_option = tk.Menu(self.menubar, tearoff = False)
            for menu_operation, operation in menu_operations.items():
                setattr(self, menu_operation, operation)
                self.menu_option.add_command(label = menu_operation, command = eval(operation))
            self.add_cascade(label = menu_option, menu = self.menu_option)

    def quit(self):
        sys.exit(0)


class RootFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, borderwidth = 5)

        # self.create_menubar()
        # self.configure(menu = self.menubar)
        self.create_layouts()
        self.place_layouts()

    def create_layouts(self):
        # self.primary_layout = ttk.Frame(self)
        self.create_tool_bar(tools) # Eventually the tool bar will change depending on mode.
        self.create_operation_panel(modes)
        self.create_status_panel(reports)
        self.create_primary_panel()
        # self.create_primary_panel(operating_mode) # = ttk.Frame(self)

    def place_layouts(self):
        self.pack(fill = 'both', expand = True)
        # self.primary_layout.pack(fill = 'both', expand = True)
        self.tool_panel.pack(side = 'top', fill = 'x')
        self.status_panel.pack(side = 'bottom',fill = 'x')
        self.operation_panel.pack(side = 'left', fill = 'y')
        self.primary_panel.pack(fill = 'both', expand = True)

    def create_primary_panel(self):
        self.primary_panel = ttk.Frame(self)
        # self.primary_panel.bg = 'red'
        self.primary_panel['relief'] = 'groove'
        # self.primary_panel['relief'] = 'sunken'
        self.primary_panel['pad'] = 10
        # self.primary_panel['style'] = self.style
        # self.primary_panel.pack(fill = 'both', expand = True)
        # self.primary_panel = ttk.Frame(self, style='background')
        self.primary_background = ttk.Label(self.primary_panel, text = '', background = 'black')
        self.primary_background.pack(fill = 'both', expand = True)

    def create_operation_panel(self, modes):
        self.operation_panel = ttk.Frame(self)
        # self.operation_panel = ttk.Frame(self.primary_layout)
        for mode, operation in modes.items():
            setattr(self, mode, operation)
            self.mode = ttk.Button(self.operation_panel, text = operation[0])
            self.mode.pack(side = 'top', fill = 'both')

    def create_status_panel(self, reports):
        pad = [0,2.5]
        self.status_panel = ttk.Frame(self, relief = tk.GROOVE)
        # self.status_panel = ttk.Frame(self.primary_layout, relief = tk.GROOVE)
        for report, status in reports.items():
            setattr(self, report, status)
            print('report: {}\t\tstatus: {}'.format(report, status))
            self.report = ttk.Label(self.status_panel, text = status[1], background = status[2], foreground = status[3])
            self.report.pack(side = status[0], padx = pad[0], pady = pad[1], fill = 'x', expand = True)

    def create_tool_bar(self, tools):
        self.tool_panel = ttk.Frame(self)
        # self.tool_panel = ttk.Frame(self.primary_layout)
        for tool, operation in tools.items():
            setattr(self, tool, operation)
            self.tool = ttk.Button(self.tool_panel, text = operation[0])
            self.tool.pack(side = 'left')

