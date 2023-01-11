# https://stackoverflow.com/questions/49956413/slicing-3d-array-list-in-python

import cv2
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


img = cv2.imread("img.png")
# img[:,0:,0] = 0
img[:,0:,1] = 0
# img[:,0:,2] = 0

plt.plot(img[:,0,0], label="Blue")
plt.plot(img[:,0,1], label="Green")
plt.plot(img[:,0,2], label="red")

cv2.imshow("frAME", img)

plt.legend()
plt.show()
cv2.waitKey(0)


# vid = cv2.VideoCapture(0)

# while True:
#     ret, frame = vid.read()
#     if ret:
#         print(frame[20:25, 30:35])
#         cv2.imshow("Frame", frame)
#         cv2.imwrite("img.png", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# vid.release()
# cv2.destroyAllWindows()