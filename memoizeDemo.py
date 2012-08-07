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
    # Create and return a memoized version of a function
    value_cache = {}
    def memoizedFunction(*args):
        if args not in value_cache:
            value_cache[args] = function(*args)
        return value_cache[args]
    return memoizedFunction # this returns a function reference - not a value


########################### Main ###############################################

if __name__ == '__main__':
    for list_length in range(10,100,10):
        
        # redefine the functions every time the loop runs to avoid time savings
        # in memoize from previous runs
        def fact(n):
            return 1 if n in [0,1] else n * fact(n-1)

        @memoize
        def memfact(n):
            return 1 if n in [0,1] else n * memfact(n-1)
        
        # generate random sequence of ints; shows the avg effect of memoization
        randSequence = range(list_length)
        random.shuffle(randSequence)

        print ('For the sequence: {}, containing {} elements.'
               .format(randSequence, len(randSequence))
               ) # show the sequence and the number of elements
        print 'Normal factorial took:'
        loop_over(fact,randSequence) # run fact on every element
        print 'Memoized factorial took:'
        loop_over(memfact,randSequence) # run memfact on every element
        print ''