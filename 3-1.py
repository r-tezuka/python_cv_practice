import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as sfft
import matplotlib.mlab as mlab
import scipy.signal as ss
# import cis
import cv2

C=cv2.imread("coins-1466263_640.jpg")
G=cv2.cvtColor(C, cv2.COLOR_BGR2GRAY)
C2=cv2.cvtColor(C, cv2.COLOR_BGR2RGB)
BW=np.zeros(G.shape)
BW[G>100]=1
R=C2.copy()
R[BW==0]=0
plt.imshow(R)
plt.show()