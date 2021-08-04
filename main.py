import pyautogui
import numpy as np
import time
while True:
    start = time.time()
    pix=np.array(pyautogui.screenshot())
    print(np.mean(pix[:,:,0]))
    print(np.mean(pix[:,:,1]))
    print(np.mean(pix[:,:,2]))
    end=time.time()
    print(end - start)