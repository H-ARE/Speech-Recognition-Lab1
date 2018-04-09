import matplotlib.pyplot as plt
import numpy as np
example = np.load('lab1_example.npz')['example'].item()
data=np.load('lab1_data.npz')['data']
a=example['frames']
print(a.shape)
plt.pcolormesh(a)
plt.show()
