from __future__ import division, print_function, unicode_literals
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

X= np.array([[2,7,9,3,10,6,1,8]]).T
Y=np.array([[13,35,41,19,45,28,10,55]]).T

plt.plot(X,Y,'ro')
plt.axis([1,10,10,55])
plt.xlabel('KM')
plt.ylabel('VND')
plt.show()