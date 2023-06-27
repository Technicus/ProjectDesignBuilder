import tkinter as tk
from tkinter import PhotoImage, Menu, ttk
from PIL import ImageTk, Image
from sys import exit
from status import status_assignment
# , status_calls #, function_mappings, status_reports
# from operator import methodcaller


class Project_Root(tk.Tk):
    from status.status_calls import callback_mouse_position, callback_null
    from status import status_calls
    print(dir(status_calls))

    def __init__(self):
        super().__init__()
        self.title('Tkinter StringVar')
        self.geometry('600x600')
        # self.attributes('-zoomed', True)
        # self.attributes('-topmost',True)
        self.event_callback_assignmet = status_assignment.event_callback_assignmet
        self.create_status_panel()

        self.image = PhotoImage(file = './image/Screen_check.png')
        self.wm_iconphoto(True, self.image)
        self.background_image = tk.Label(self, i = self.image)
        self.background_image.pack(fill='both', expand='yes')


    def create_status_panel(self):
        pad = [0,2.5]
        self.status_panel = ttk.Frame(self, relief = tk.GROOVE)
        for event_call, status in self.event_callback_assignmet.items():
            setattr(self, event_call, status)
            self.event_callback_assignmet[event_call]['status_var'] = tk.StringVar()
            self.event_callback_assignmet[event_call]['status_var'].set(self.event_callback_assignmet[event_call]['configure']['text'])
            self.event_callback_assignmet[event_call]['label'] = ttk.Label(
                self.status_panel,
                text = self.event_callback_assignmet[event_call]['status_var'].get(),
                background = self.event_callback_assignmet[event_call]['configure']['background'],
                foreground = self.event_callback_assignmet[event_call]['configure']['foreground']
                )
            self.event_callback_assignmet[event_call]['label'].pack(
                side = self.event_callback_assignmet[event_call]['configure']['side'],
                padx = self.event_callback_assignmet[event_call]['configure']['pad'][0],
                pady = self.event_callback_assignmet[event_call]['configure']['pad'][1],
                fill = self.event_callback_assignmet[event_call]['configure']['fill'],
                expand = self.event_callback_assignmet[event_call]['configure']['expand']
                )
            print('self.event_callback_assignmet[event_call][\'status_var\']: {}'.format(self.event_callback_assignmet[event_call]['status_var']))
            print('event: {}'.format(self.event_callback_assignmet[event_call]['event']))
            print('callback: {}'.format(self.event_callback_assignmet[event_call]['callback']))
            self.event_callback_assignmet[event_call]['callback'] = eval('self.' + self.event_callback_assignmet[event_call]['callback'])
            self.bind(self.event_callback_assignmet[event_call]['event'], self.event_callback_assignmet[event_call]['callback'])
        self.status_panel.pack(side = 'bottom',fill = 'x')


if __name__ == '__main__':
    project_root = Project_Root()
    project_root.mainloop()