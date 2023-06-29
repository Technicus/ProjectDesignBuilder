from functools import wraps
import sys
import os

# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)

# adding the parent directory to
# the sys.path.
sys.path.append(parent)

# now we can import the module in the parent
# directory.
# import status.status_calls
# from status import status_calls
from status import status_calls

class Project_Root():
    def __init__(self):
        super().__init__()
        # pass
        # status_calls.callback_null
        # from status import status_calls
        # setattr(self, 'callback_null', status_calls.callback_null)
        # for key, value in status_calls.callbacks.items:
            # print('{}: {}'.format(key, value))
        # print(status_calls.callbacks.keys())
        # for key, value in status_calls.callbacks.items():
        #     print('{}: {}'.format(key, value))
        #     setattr(self, key, value)

        # setattr(self, status_calls.callbacks.keys()['callback_null'], status_calls.callbacks['callback_null'])
        # for method in dir(status_calls):
        #     if not method.startswith('__'):
        #     # print(method)
        #     add_method(project_root)

    def locals_query(self):
        for key, value in locals().copy().items():
            if not key.startswith('__'):
                print('key: {}'.format(key))
                print('value: {}'.format(value))
                print('type: {}\n'.format(type(value)))

    # def function_to_method(self, func, clas, method_name=None):
    # def function_to_method(self, func, method_name = 'null'):
    #     # setattr(clas, method_name, func)
    #     setattr(self, method_name, func)
if __name__ == '__main__':
    project_root = Project_Root()
    # project_root.locals_query()

    # print(status_calls.callbacks.keys())
    # for key, value in status_calls.callbacks.items():
    #     # print('{}: {}'.format(key, value))
    #     setattr(project_root, key, value)

    # project_root.locals_query()


# class Project_Method():
#     def __init__(self):
#         super().__init__()
#         print(f'Project_Method():\n{locals()}\n')
#
#         pass
#
#
#     def add_method(cls):
#         def decorator(func):
#             @wraps(func)
#             def wrapper(self, *args, **kwargs):
#                 return func(*args, **kwargs)
#             setattr(cls, func.__name__, wrapper)
#             # Note we are not binding func, but wrapper which accepts self but does exactly the same as func
#             return func # returning func means func can still be used normally
#         return decorator
#
#
#     def import_statuscalls(cls):
#         # from status import status_calls
#         # print(locals())
#         for method in dir(status_calls):
#             if not method.startswith('__'):
#                 # print(f'{method}: {type(method)}')
#                 print(method)
#                 im = importlib.import_module(method)
#                 # setattr(self, method.__name__, method)
#                 # self.list_callback_methods()
#         print(f'import_statuscalls()():\n{locals()}\n')
#
#     # print('locals()[\'add_method\']:\n{}\n\nlocals()[\'import_statuscalls\']:\n{}\n\nlocals():\n{}\n'.format(locals()['add_method'], locals()['import_statuscalls'], locals()))
#
# def add_method(cls):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(self, *args, **kwargs):
#             return func(*args, **kwargs)
#         setattr(cls, func.__name__, wrapper)
#         # Note we are not binding func, but wrapper which accepts self but does exactly the same as func
#         return func # returning func means func can still be used normally
#     return decorator

# if __name__ == '__main__':
#     project_root = Project_Root()
#     project_root.locals_query()
    # project_root.callback_null('self', 'value')
    #project_root
    # for key, value in project_root.locals().copy().items():
    # # # for key, value in status_calls.locals().copy().items():
    #     if not key.startswith('__'):
    #         print('key: {}'.format(key))
    #         print('value: {}'.format(value))
    #         print('type: {}\n'.format(type(value)))
    #
    # for method in dir(status_calls):
    #     if not method.startswith('__'):
    #         print(method)
    #         add_method(project_root)
    #         # function_to_method(self, func, clas, method_name=None):
    #         # function_to_method(self, func, method_name = 'null'):
    #
    #         project_root.function_to_method(method)
            # from status.status_calls import method
    # print()
    # status_calls.callback_null('self', 'value')
#
    # project_root.locals_query()



    # for key, value in locals().copy().items():status.status_calls
    # for key, value in status.status_calls.locals().copy().items():
    #         if not key.startswith('__'):
    #             print('key: {}'.format(key))
    #             print('value: {}'.format(value))
    #             print('type: {}\n'.format(type(value)))

    # project_method = Project_Method()
    # print('locals()[\'project_root\']:\n{}\n\nlocals()[\'project_method\']:\n{}\n\nlocals():\n{}\n'.format(locals()['project_root'], locals()['project_method'], locals()))
    # print('Classes:')
    # this = {}
    # local_keys = locals().keys()

    # for key in local_keys:
        # print('{}'.format(key))
    # for key, value in locals().copy().items():
    #     # if type(value) == 'type':
    #     if not key.startswith('__'):
    #         print('key: {}'.format(key))
    #         print('value: {}'.format(value))
    #         print('type: {}\n'.format(type(value)))
    #         # print('{}: {}'.format( key, value))
    #         # print('{} -> {}: {}'.format(type(value), key, value))
    # print('')
