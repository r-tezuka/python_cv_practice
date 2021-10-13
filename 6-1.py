import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as ss
import scipy.ndimage.filters as sfil
import cis
import cv2

G=np.uint8(180*np.ones((256,256)))
cv2.imread('cyclist-394274_640.jpg',0)
cis.mesh(G)