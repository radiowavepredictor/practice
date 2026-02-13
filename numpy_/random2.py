from numpy.random import RandomState

def return_rand(rnd:RandomState):
    return rnd.rand()

rnd=RandomState(0)

for i in range(5):
    print(return_rand(rnd))