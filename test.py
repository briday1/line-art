import numpy as np
import matplotlib.pyplot as plt

# Create an image 
M, N = 9, 9
img = np.zeros((M,N))
img[3:6, 3:6] = 1