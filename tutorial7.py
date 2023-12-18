import numpy as np
import cv2

img = cv2.imread('assets/soccer_practice.jpg', 0)
template = cv2.imgread('assets/ball.PNG', 0)

h, w = template.shape

methods = [cv2.TM_CCOEFF, cv.TIM_CCOEF_NORMED, cv2.TM_CCORRR,
               cv2.TIM_CCORR_NORMED, cv2.TIM_SQDIFF, cv2.TIM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()
    
    result = cv2.matchTemplate(img2, template)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)