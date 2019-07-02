import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('noise.jpg',0)
final = img[:]

plt.subplot(1,2,1)
plt.title('ORIGINAL')
plt.xticks([])
plt.yticks([])
plt.imshow(img)

for x in range(0, img.shape[0]):
	for y in range(0, img.shape[1]):
		final[x,y] = img[x,y]

arr = [img[0,0]]*9
for x in range(1,img.shape[0]-1):
	for y in range(1, img.shape[1]-1):
		arr[0] = img[x-1,y-1]
		arr[1] = img[x,y-1]
		arr[2] = img[x+1,y-1]
		arr[3] = img[x-1,y]
		arr[4] = img[x,y]
		arr[5] = img[x+1,y]
		arr[6] = img[x-1,y+1]
		arr[7] = img[x,y+1]
		arr[8] = img[x+1,y+1]

		arr.sort()
		final[x,y] = arr[4]
		img1 = img

plt.subplot(1,2,2) 
plt.title('Med_blur')
plt.xticks([])
plt.yticks([])
plt.imshow(img1)

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

