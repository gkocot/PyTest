import cv2
import numpy as np
import math

img1 = cv2.imread('test250up.jpg')
#img1 = cv2.imread('garage_down.jpg')
W1, H1, planes1 = img1.shape

# TBD: make phi0, theta0 center of the perspective
FOV = math.pi / 8
phi0 = math.pi / 4
theta0 = 0

print('img1: ', W1, "x", H1)

img2 = np.zeros((400, 300, 3), 'uint8')
W2, H2, planes2 = img2.shape

print('img2: ', W2, "x", H2)

while True:
    for y2 in range(H2):
        phi = phi0 + FOV * y2 / H2
        for x2 in range(W2):
            theta = theta0 + FOV * x2 / H2
            u = math.cos(phi) * math.cos(theta)
            v = math.cos(phi) * math.sin(theta)
            x1 = int(((u + 1) / 2) * (W1 - 1))
            y1 = int(((v + 1) / 2) * (H1 - 1))
            # x1 = Cx + int((u + 1) * r)
            # y1 = Cy + int((v + 1) * r)
            img2[x2, y2] = img1[int(x1), int(y1)]
            
    wnd1 = cv2.namedWindow('wnd1', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('wnd1', 300, 300)        
    cv2.imshow('wnd1', img1)        
            
    wnd2 = cv2.namedWindow('wnd2', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('wnd2', cv2.rotate(img2, cv2.ROTATE_90_COUNTERCLOCKWISE))

    key = cv2.waitKey(0)
    if key == ord('o'):
        FOV = FOV + math.pi / 16
    if key == ord('p'):
        FOV = FOV - math.pi / 16
    if key == ord('i'):
        phi0 = phi0 + math.pi / 32
    if key == ord('k'):
        phi0 = phi0 - math.pi / 32
    if key == ord('l'):
        theta0 = theta0 + math.pi / 32
    if key == ord('j'):
        theta0 = theta0 - math.pi / 32
    if key == ord('q'):
        break
    
    
cv2.destroyAllWindows()