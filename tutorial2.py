import cv2
# import random


img = cv2.imread("assets/logo.jpg", -1)

# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

tag = img[361:495, 354:632]
# ROW1:ROW2 [x1:x2], COL1:COL2 [y1:y2]
# Logo is 271px WIDE X 141px HIGH
img[0:134, 0:278] = tag
# 495-361 = 134
# 632 - 354 = 278
        
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
