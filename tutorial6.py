import numpy as np
import cv2

img = cv2.imread("assets/chessboard.png")
img = cv2.resize(img, (0,0), fx=0.75, fy=0.75)
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(grey, 100, 0.01, 10)
corners = np.int_(corners)

for corner in corners:
    x,y = corner.ravel()
#     print(x,y)
    cv2.circle(img, (x,y), 5, (255,0,0), -1)

for i in range(len(corners)):
    for j in range(i+ 1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
#         print(corner1, corner2)
        #color = tuple(list(np.random.choice(range(256), size=3)))
        color = list(np.random.random(size=3)*256)
#       
#         print(color)
        cv2.line(img, corner1, corner2, color, 1)

cv2.imshow('frame',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
