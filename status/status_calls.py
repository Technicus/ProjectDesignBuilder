# def callback_mouse_position(value):
#     x = value.x
#     y = value.y
#     mouse_position = str(str(x) + ',' + str(y))
#     # print("mouse_position: {}".format(mouse_position))
#     print("value: {}".format(value))
#     self.status_var['mouse_position'].set(mouse_position)
#     self.report['mouse_position'].config(text=self.status_var['mouse_position'].get())

# def callback_mouse_position(self, value):
#      x = value.x
#      y = value.y
#      mouse_position = str(str(x) + ',' + str(y))
#      self.event_callback_assignmet['mouse_position']['status_var'].set(mouse_position)
#      self.event_callback_assignmet['mouse_position']['label'].config(text = self.event_callback_assignmet['mouse_position']['status_var'].get())
#      print('mouse_position: {}'.format(mouse_position))

def callback_mouse_position(self, value):
    x = value.x
    y = value.y
    mouse_position = str(str(x) + ',' + str(y))
    self.event_callback_assignmet['mouse_position']['status_var'].set(mouse_position)
    self.event_callback_assignmet['mouse_position']['label'].config(text = self.event_callback_assignmet['mouse_position']['status_var'].get())
    print('mouse_position: {}'.format(mouse_position))


def callback_mousewheel_up(self, value):
    print("callback_mousewheel_up: {}".format(value))


def callback_mousewheel_down(self, value):
    print("callback_mousewheel_down: {}".format(value))


def callback_button_1(self, value):
    print("callback_button_1: {}".format(value))


def callback_double_button_1(self, value):
    print("callback_double_button_1: {}".format(value))


def callback_triple_button_1(self, value):
    print("callback_triple_button_1: {}".format(value))


def callback_button_2(self, value):
    print("callback_button_2: {}".format(value))


def callback_double_button_2(self, value):
    print("callback_double_button_2: {}".format(value))


def callback_triple_button_2(self, value):
    print("callback_triple_button_2: {}".format(value))


def callback_button_3(self, value):
    print("callback_button_3: {}".format(value))


def callback_double_button_3(self, value):
    print("callback_double_button_3: {}".format(value))


def callback_triple_button_3(self, value):
    print("callback_triple_button_3: {}".format(value))


def callback_key_pressed(self, value):
    pass


def callback_null(self, value):
    pass


