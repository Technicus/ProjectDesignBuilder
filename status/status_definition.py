
# # This dictionary provides definition for status output.
# # Each status section is identified by the key name, and the list assigned to each name will provide text, what action to report, and function to call.
event_callback_config = {
            'mouse_position': {
                'event': '<Motion>',
                'callback': 'callback_mouse_position',
                'data': '',
                'configure':{
                    'parent': 'self.status_panel',
                    'side': 'left',
                    'fill': 'x',
                    'expand': True,
                    'pad': [0, 0],
                    'background': 'orange',
                    'foreground': 'black',
                    'text': 'Mouse Position'
                        }
                }
            }

report = {
    # 'message': {
    #     # 'event': ['<Enter>', '<Leave>'],
    #     'event': '<Enter>',
    #     'callback': 'callback_null',
    #     'configure':{
    #         'parent': 'self.status_panel',
    #         'side': 'bottom',
    #         'fill': 'x',
    #         'expand': True,
    #         'pad': [0, 0],
    #         'background': 'black',
    #         'foreground': 'white',
    #         'text': 'message_null'
    #             }
    #     },
    'mouse_position': {
        'event': '<Motion>',
        'callback': 'callback_mouse_position',
        'configure':{
            'parent': 'self.status_panel',
            'side': 'left',
            'fill': 'x',
            'expand': True,
            'pad': [0, 0],
            'background': 'orange',
            'foreground': 'black',
            'text': 'Mouse Position'
                }
        }
    }

# report = {
#     'message': {
#         # 'event': ['<Enter>', '<Leave>'],
#         'event': '<Enter>',
#         'callback': 'callback_null',
#         'configure':{
#             'parent': 'self.status_panel',
#             'side': 'bottom',
#             'fill': 'x',
#             'expand': True,
#             'pad': [0, 0],
#             'background': 'black',
#             'foreground': 'white',
#             'text': 'message_null'
#                 }
#         },
#     'menu': {
#         # 'event': ['<FocusIn>', '<FocusOut>'],
#         'event': '<FocusIn>',
#         'callback': 'callback_null',
#         'configure':{
#             'parent': 'self.status_panel',
#             'side': 'left',
#             'fill': 'x',
#             'expand': True,
#             'pad': [0, 0],
#             'background': 'grey',
#             'foreground': 'white',
#             'text': 'menu_null'
#                 }
#         },
#     'mouse_position': {
#         'event': '<Motion>',
#         'callback': 'callback_mouse_position',
#         'configure':{
#             'parent': 'self.status_panel',
#             'side': 'left',
#             'fill': 'x',
#             'expand': True,
#             'pad': [0, 0],
#             'background': 'orange',
#             'foreground': 'black',
#             'text': 'Mouse Position'
#                 }
#         },
#     'mouse_wheel_up': {
#         'event': '<Button-4>',
#         'callback': 'callback_mousewheel_up',
#         'configure':{
#             'parent': 'self.status_panel',
#             'side': 'left',
#             'fill': 'x',
#             'expand': True,
#             'pad': [0, 0],
#             'background': 'yellow',
#             'foreground': 'red',
#             'text': 'Mouse Wheel'
#                 }
#         },
#     'mouse_wheel_down': {
#         'event': '<Button-5>',
#         'callback': 'callback_mousewheel_down',
#         'configure':{
#             'parent': 'self.status_panel',
#             'side': 'left',
#             'fill': 'x',
#             'expand': True,
#             'pad': [0, 0],
#             'background': 'yellow',
#             'foreground': 'red',
#             'text': 'Mouse Wheel'
#                 }
#         },
#     'mouse_button_left_1': {
#         'event': '<Button-1>',
#         'callback': 'callback_button_1',
#         'configure':{
#             'parent': 'self.status_panel',
#             'side': 'left',
#             'fill': 'x',
#             'expand': True,
#             'pad': [0, 0],
#             'background': 'red',
#             'foreground': 'white',
#             'text': 'Mouse Left_1'
#                 }
#         },
#     'mouse_button_left_2': {
#         'event': '<Double-Button-1>',
#         'callback': 'callback_button_1_double',
#         'configure':{
#             'parent': 'self.status_panel',
#             'side': 'left',
#             'fill': 'x',
#             'expand': True,
#             'pad': [0, 0],
#             'background': 'red',
#             'foreground': 'white',
#             'text': 'Mouse Left_2'
#                 }
#         },
#     'mouse_button_left_3': {
#         'event': '<Triple-Button-1>',
#         'callback': 'callback_button_1_triple',
#         'configure':{
#             'parent': 'self.status_panel',
#             'side': 'left',
#             'fill': 'x',
#             'expand': True,
#             'pad': [0, 0],
#             'background': 'red',
#             'foreground': 'white',
#             'text': 'Mouse Left_3'
#                 }
#         },
#     'mouse_button_middle_1': {
#         'event': '<Button-2>',
#         'callback': 'callback_button_2',
#         'configure':{
#             'parent': 'self.status_panel',
#             'side': 'left',
#             'fill': 'x',
#             'expand': True,
#             'pad': [0, 0],
#             'background': 'purple',
#             'foreground': 'white',
#             'text': 'Mouse Middle_1'
#                 }
#         },
#     'mouse_button_middle_2': {
#         'event': '<Double-Button-2>',
#         'callback': 'callback_button_2_double',
#         'configure':{
#             'parent': 'self.status_panel',
#             'side': 'left',
#             'fill': 'x',
#             'expand': True,
#             'pad': [0, 0],
#             'background': 'purple',
#             'foreground': 'white',
#             'text': 'Mouse Middle_2'
#                 }
#         },
#     'mouse_button_middle_3': {
#         'event': '<Triple-Button-2>',
#         'callback': 'callback_button_2_triple',
#         'configure':{
#             'parent': 'self.status_panel',
#             'side': 'left',
#             'fill': 'x',
#             'expand': True,
#             'pad': [0, 0],
#             'background': 'purple',
#             'foreground': 'white',
#             'text': 'Mouse Middle_3'
#                 }
#         },
#     'mouse_button_right_1': {
#         'event': '<Button-3>',
#         'callback': 'callback_button_3',
#         'configure':{
#             'parent': 'self.status_panel',
#             'side': 'left',
#             'fill': 'x',
#             'expand': True,
#             'pad': [0, 0],
#             'background': 'blue',
#             'foreground': 'white',
#             'text': 'Mouse Right_1'
#                 }
#         },
#     'mouse_button_right_2': {
#         'event': '<Double-Button-3>',
#         'callback': 'callback_button_3_double',
#         'configure':{
#             'parent': 'self.status_panel',
#             'side': 'left',
#             'fill': 'x',
#             'expand': True,
#             'pad': [0, 0],
#             'background': 'blue',
#             'foreground': 'white',
#             'text': 'Mouse Right_2'
#                 }
#         },
#     'mouse_button_right_3': {
#         'event': '<Triple-Button-3>',
#         'callback': 'callback_button_3_triple',
#         'configure':{
#             'parent': 'self.status_panel',
#             'side': 'left',
#             'fill': 'x',
#             'expand': True,
#             'pad': [0, 0],
#             'background': 'blue',
#             'foreground': 'white',
#             'text': 'Mouse Right_3'
#                 }
#         },
#     'keyboard': {
#         'event': '<Key>',
#         'callback': 'callback_null',
#         'configure':{
#             'parent': 'self.status_panel',
#             'side': 'left',
#             'fill': 'x',
#             'expand': True,
#             'pad': [0, 0],
#             'background': 'green',
#             'foreground': 'white',
#             'text': 'keyboard'
#                 }
#         },
#     'enter': {
#         'event': '<Enter>',
#         'callback': 'callback_null',
#         'configure':{
#             'parent': 'self.status_panel',
#             'side': 'left',
#             'fill': 'x',
#             'expand': True,
#             'pad': [0, 0],
#             'background': 'brown',
#             'foreground': 'white',
#             'text': 'enter'
#                 }
#         },
#     'leave': {
#         'event': '<Leave>',
#         'callback': 'callback_null',
#         'configure':{
#             'parent': 'self.status_panel',
#             'side': 'left',
#             'fill': 'x',
#             'expand': True,
#             'pad': [0, 0],
#             'background': 'brown',
#             'foreground': 'white',
#             'text': 'leave'
#                 }
#         },
#     }