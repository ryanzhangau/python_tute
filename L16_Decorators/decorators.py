# Decorators accept a function and extend the behaviour of the function but not editing the function
# It is a wrapper function

def cough_dec(func):
    def func_wrapper():
        # code before function
        print('*Cough*')
        func()
        # code after function
        print('*Cough*')

    return func_wrapper


@cough_dec
def question():
    print('Can you give me a discount on that?')


question()
