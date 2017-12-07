#!/usr/bin/python
import sys
sys.path.append('/usr/local/lib/python3.6/site-packages')
import cv2
from pylab import *
from matplotlib import pyplot as plt


band = cv2.imread("l7_ms.tif")

blur = cv2.blur(band,(5,5))
median = cv2.medianBlur(band,5)

plt.subplot(121),plt.imshow(band),plt.title('Landsat 7 TM yakın Kızıl Ötesi bandı')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('After Mean Filter 5x5')
plt.xticks([]), plt.yticks([])
savefig("BeforeAfterMeanFilter.tif")
plt.show()


plt.subplot(121),plt.imshow(band),plt.title('Landsat 7 TM yakın Kızıl Ötesi bandı')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('After Median Filter 5x5')
plt.xticks([]), plt.yticks([])
savefig("BeforeAfterMedianFilter.tif")
plt.show()
