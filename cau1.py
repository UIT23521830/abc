import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = 2 * np.random.rand(100,1)
y = 4 + 3 * x + np.random.randn(100,1) 

bias_term = np.ones((100,1))
x_b = np.c_[bias_term,x]
#X_b = np.c_[np.ones((100, 1)), x]

plt.scatter(x, y, color='blue', marker='o')
plt.show(block=True)

x_b.shape
y.shape