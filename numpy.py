import numpy as np

import random
def variables():
     values=random.randint(1,30)
     print(values)
     varaible2 =random.randint(1,30)
     print(varaible2)
     
    
variables()

def ints():
    value =random.randint(1,10)
    print(value)
    value_2 = random.random()
    print(value_2)
    value_3 = random.choice([1,2,3,4,5])
    print(value_3)
    value_4 = random.uniform(1.0,5.0)
    print(value_4)
ints()
def variables():
     values=random.randint(1,30)
     print(values)
     varaible2 =random.randint(1,30)
     print(varaible2)
     
    
variables()

vector = np.array([3, 4])
norm = np.linalg.norm(vector)
print(norm)