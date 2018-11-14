import cv2
import numpy as np
import math

# img1 = cv2.imread('test250up.jpg')
img1 = cv2.imread('garage_down.jpg')
W1, H1, planes1 = img1.shape

print('img1: ', W1, "x", H1)

img2 = np.zeros((900, 300, 3), 'uint8')
W2, H2, planes2 = img2.shape

print('img2: ', W2, "x", H2)

for y2 in range(H2):
    phi = y2 / H2 * math.pi / 2
    for x2 in range(W2):
        theta = x2 / W2 * math.pi * 2
        # top sphere (fisheye mounting point)
        #u = (1 - math.cos(phi)) * math.cos(theta)
        #v = (1 - math.cos(phi)) * math.sin(theta)
        # bottom sphere (fisheye mounting point)
        u = (math.cos(phi)) * math.cos(theta)
        v = (math.cos(phi)) * math.sin(theta)
        x1 = int(((u + 1) / 2) * (W1 - 1))
        y1 = int(((v + 1) / 2) * (H1 - 1))
        # x1 = Cx + int((u + 1) * r)
        # y1 = Cy + int((v + 1) * r)
        img2[x2, y2] = img1[int(x1), int(y1)]
        
wnd1 = cv2.namedWindow('wnd1', cv2.WINDOW_NORMAL)
cv2.resizeWindow('wnd1', 300, 300)        
cv2.imshow('wnd1', img1)        
        
wnd2 = cv2.namedWindow('wnd2', cv2.WINDOW_AUTOSIZE)
cv2.imshow('wnd2', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()