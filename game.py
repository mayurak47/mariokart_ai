import numpy as np
import cv2
from mss import mss
from PIL import Image
import time
import pyautogui

def process_img(original_img):
    processed_img = cv2.cvtColor(np.array(original_img), cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    return processed_img

for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

from try1 import PressKey, S

PressKey(S)
# print('down')
# for i in range(50):
#     pyautogui.press('s')
# time.sleep(10)
# print('up')
# pyautogui.keyUp('s')

# mon = {'top': 40, 'left': 0, 'width': 485, 'height': 354}
#
# sct = mss()
#
# last_time = time.time()
#
# while 1:
#     print('Loop took {} seconds'.format(time.time()-last_time))
#     last_time = time.time()
#     sct.get_pixels(mon)
#     img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
#     new_img = process_img(img)
#     cv2.imshow('window', new_img)
#     # cv2.imshow('test', np.array(img))
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break
