






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
# def callback_null():
    print('callback_null')
    for key, value in locals().copy().items():
        if not key.startswith('__'):
            print('key: {}'.format(key))
            print('value: {}'.format(value))
            print('type: {}\n'.format(type(value)))


from functools import wraps # This convenience func preserves name and docstring
def add_method(cls):
    def decorator(func):
        @wraps(func)
            def wrapper(self, *args, **kwargs):
            return func(*args, **kwargs)
            setattr(cls, func.__name__, wrapper)
        # Note we are not binding func, but wrapper which accepts self but does exactly the same as func
        return func # returning func means func can still be used normally
    return decorator

class Calls():
    def __init__(self):
        # super().__init__()
        # calls = {}
        pass

    # def add_method(cls):
    #     from functools import wraps # This convenience func preserves name and docstring
    #     def decorator(func):
    #         @wraps(func)
    #         def wrapper(self, *args, **kwargs):
    #             return func(*args, **kwargs)
    #         setattr(cls, func.__name__, wrapper)
    #         # Note we are not binding func, but wrapper which accepts self but does exactly the same as func
    #         return func # returning func means func can still be used normally
    #     return decorator

    def locals_query(self):
        for key, value in locals().copy().items():
            if not key.startswith('__'):
                print('key: {}'.format(key))
                print('value: {}'.format(value))
                # print('type: {}\n'.format(type(value)))
        #         calls[key] = value

# for key, value in locals().copy().items():
calls = Calls()
for key, value in locals().copy().items():
    if not key.startswith('__') and not key == 'Calls' and not key == 'calls':
        # print('key: {}'.format(key))
        # print('value: {}'.format(value))
        # print('type: {}\n'.format(type(value)))
        setattr(calls, key, value)
        # calls[key] = value
calls.locals_query()
# callbacks = {
#     'callback_button_1' = callback_button_1
#     'callback_button_2' = callback_button_2
#     'callback_button_3' = callback_button_3
#     'callback_double_button_1' = callback_double_button_1
#     'callback_double_button_2' = callback_double_button_2
#     'callback_double_button_3' = callback_double_button_3
#     'callback_key_pressed' = callback_key_pressed
#     'callback_mouse_position' = callback_mouse_position
#     'callback_mousewheel_down' = callback_mousewheel_down
#     'callback_mousewheel_up' = callback_mousewheel_up
#     'callback_null' = callback_null
#     'callback_triple_button_1' = callback_triple_button_1
#     'callback_triple_button_2' = callback_triple_button_2
#     'callback_triple_button_3' = callback_triple_button_3
#     }