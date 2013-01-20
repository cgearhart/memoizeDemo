from functools import wraps
import random
import time

########################### Helper Functions ###################################

def print_timing(func):
    def wrapper(*arg):
        t1 = time.time()
        res = func(*arg)
        t2 = time.time()
        print '{:0.3f} ms'.format((t2-t1)*1000.0)
        return res
    return wrapper

@print_timing
def loop_over(func,list):
    return map(func,list)


########################### Memoize Function ###################################

def memoize(function):
    value_cache = {}
    @wraps #preserve docstring, etc.
    def memoizedFunction(*args):
        if args not in value_cache:
            value_cache[args] = function(*args)
        return value_cache[args]
    return memoizedFunction
            

########################### Main ###############################################

if __name__ == '__main__':

    def fib(n):
        return n if n in [0,1] else fib(n-1) + fib(n-2)

    @memoize
    def memfib(n):
        return n if n in [0,1] else memfib(n-1) + memfib(n-2)
    
    sequence = range(30) # Warning! range(40) takes several minutes to run
    print 'For {} elements:'.format(len(sequence))
    print 'Normal fib took:'
    loop_over(fib,sequence) # approx average 2080 ms for 30 elements
    print 'Memoized fib took:'
    loop_over(memfib,sequence) # approx average .126 ms for 30 elements
    print ''


