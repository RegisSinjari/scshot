import pyautogui
import numpy as np
from numba import jit
import time
start = time.time()
myScreenshot = pyautogui.screenshot()
pix=np.array(myScreenshot,dtype=np.float32)


@jit(nopython=True)
def counter(pixa):
    sumex,sumey,sumez,counter = 0,0,0,0
    for line in pixa:
        for lines in line:
            sumex += lines[0]
            sumey += lines[1]
            sumez += lines[2]
            counter+=1
    return [round(sumex/counter),round(sumey/counter),round(sumez/counter)]

def outer(pixa):
    top=pixa[:,0]
    left=pixa[0,:]
    right=pixa[:-1]

def mostly(a):
    if a[1]<a[0]>a[2]:
        return 'R'
    elif a[0]<a[1]>a[2]:
        return 'G'
    elif a[0]<a[2]>a[1]:
        return 'B'
print(counter(pix))
end=time.time()
print(end - start)