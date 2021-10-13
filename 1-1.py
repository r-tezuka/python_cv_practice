import numpy as np
import matplotlib.pyplot as plt

t=np.arange(0,1,1/8000)
a=0.8
f=440
y=a*np.sin(2*np.pi*f*t)

plt.plot(t,y)
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.show()