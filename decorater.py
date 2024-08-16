import time 

def timer(func):
    def wraper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} is run in {end-start}")
        return result
    return wraper 
@timer
def example_func(w):
    time.sleep(w)
example_func(2)
