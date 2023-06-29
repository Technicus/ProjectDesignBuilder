# https://www.oreilly.com/library/view/python-cookbook/0596001673/ch05s13.html

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
import status.status_calls

def list_methods(cls):
    print('{} methods:'.format(cls))
    for method in dir(cls):
        if not method.startswith('__'):
            print(method)
    print()


def test_function(test = 'empty test'):
    print('test_function: {}\n'.format(test))
    return 'tested'


class Test_Class():

    def funcToMethod(self, func, clas, method_name=None):
        setattr(clas, method_name, func)


if __name__ == '__main__':
    test_function('not a class method')
    test_class = Test_Class()
    list_methods(test_class)
    test_class.funcToMethod(test_function, test_class, 'test_method')
    test_class.funcToMethod(status.status_calls.callback_null, test_class, 'callback_null')
    list_methods(test_class)
    test_class.test_method('this is a class method')