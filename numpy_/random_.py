import numpy as np

rnd = np.random.RandomState(0)

for _ in range(5):
    print(rnd.rand())