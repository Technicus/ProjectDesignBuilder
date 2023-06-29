# https://mgarod.medium.com/dynamically-add-a-method-to-a-class-in-python-c49204b85bd6


from functools import wraps # This convenience func preserves name and docstring

class A:
    pass

def add_method(cls):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            return func(*args, **kwargs)
        setattr(cls, func.__name__, wrapper)
        # Note we are not binding func, but wrapper which accepts self but does exactly the same as func
        return func # returning func means func can still be used normally
    return decorator

# No trickery. Class A has no methods nor variables.
a = A()
try:
    a.foo()
except AttributeError as ae:
    print(f'Exception caught: {ae}') # 'A' object has no attribute 'foo'

try:
    a.bar('The quick brown fox jumped over the lazy dog.')
except AttributeError as ae:
    print(f'Exception caught: {ae}') # 'A' object has no attribute 'bar'

# Non-decorator way (note the function must accept self)
# def foo(self):
#     print('hello world!')
# setattr(A, 'foo', foo)

# def bar(self, s):
#     print(f'Message: {s}')
# setattr(A, 'bar', bar)

# Decorator can be written to take normal functions and make them methods
@add_method(A)
def foo():
    print('hello world!')

@add_method(A)
def bar(s):
    print(f'Message: {s}')

def another_function(input = None):
    print(f'\nanother function for experimenting with\n')
    if input:
        print(f'the input provided is: {input}')
    return 'supper is ready'

a.foo()
a.bar('The quick brown fox jumped over the lazy dog.')
print(a.foo) # <bound method foo of <__main__.A object at {ADDRESS}>>
print(a.bar) # <bound method bar of <__main__.A object at {ADDRESS}>>

# foo and bar are still usable as functions
foo()
bar('The quick brown fox jumped over the lazy dog.')
print(foo) # <function foo at {ADDRESS}>
print(bar) # <function bar at {ADDRESS}>

print(locals()['another_function'])
print(locals()['another_function']())
print(type(another_function()))
locals()['another_function']
locals()['another_function']('guess what')



print()
print(type(locals))
print(type(locals()))
print(locals())
print(locals()['add_method'])
# # print(type(local_))
# local_ = locals()
# # for key, value in local_.items():
# for key in local_.keys():
#     # print(locals())
#     print('key: {} '.format(key))
#     # print('{} : {} : {}'.format(key, value, type(value)))
