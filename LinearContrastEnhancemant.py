#!/usr/bin/python
import sys
sys.path.append('/usr/local/lib/python3.6/site-packages')
import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from pylab import *

BitNumber=8
Quantk=2**BitNumber #range independence of pixel value
bands=["Irvine_TM_B1.tif","Irvine_TM_B2.tif","Irvine_TM_B3.tif","Irvine_TM_B4.tif"] #bands name list
linearContrastEnhancemantNameList=["Band1.tif","Band2.tif","Band3.tif","Band4.tif"] #new bands name list
for lIN in range(4): #lIN list Index Number
    band=bands[lIN] #sırayla sitring olarak band isimlerini alıyor
    bandx=cv2.imread(band,0) #band isimlerine göre dizindeki bandları okuyor

    BVmin=bandx.min() #okuduğu bandtaki minumum pixel değerini buluyor
    BVmax=bandx.max() #max pixel value of reading band
    pixelNumber=len(bandx) #bandta tek dizindeki satır sayısını veriyor
    for i in range (pixelNumber):
        for j in range (pixelNumber):
            BVin=bandx[i,j] # pixel value

            BVout=int(((BVin-BVmin)/(BVmax-BVmin))*Quantk) #formule of the linearContrastEnhancemant
            bandx[i,j]=BVout

    linearContrastEnhancemantList=[] #linear Contrast Enhancemant List
    linearContrastEnhancemantList.append(bandx) #add new band to linear Contrast Enhancemant List
    NewBandName=linearContrastEnhancemantNameList[lIN]
    cv2.imwrite(NewBandName,bandx) #create new .fit
