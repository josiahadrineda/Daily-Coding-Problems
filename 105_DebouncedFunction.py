import time

def debounced_function(f):
    def specify_args(*args, **kwargs):
        def sleep_then_call(N):
            time.sleep(N / 1000)
            return f(*args, **kwargs)
        return sleep_then_call
    return specify_args

@debounced_function
def i_love_you():
    print('I love you!')

# First set of parens = func args
# 3000 ms = 3 secs
i_love_you()(3000)