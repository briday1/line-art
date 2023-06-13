import numpy as np
import matplotlib.pyplot as plt
plt.ion()

# Create an image 
M, N = 9, 9
img = np.zeros((M,N))
img[3:6, 3:6] = 1

plt.figure()
plt.imshow(img)