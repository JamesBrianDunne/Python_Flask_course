

def my_method(arg1, arg2):
    return arg1 + arg2


my_method(5, 6)


def addition_simplified(*args):
    return sum(args)


def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


what_are_kwargs(12, 34, 56, name='Jose', location='UK')
