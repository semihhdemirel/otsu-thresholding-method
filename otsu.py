from cv2 import cv2 
import numpy as np
import math
ROOTDIR="/../../"#Directory of an image
img = cv2.imread(ROOTDIR,0)#imread the image as grayscale
cv2.imshow("image",img)
piksel_values=np.zeros([1,256])
for i in range(0,256):
    piksel_values[0,i]=i
histr = cv2.calcHist([img],[0],None,[256],[0,256])#histogram of the image
histr=np.transpose(histr)
rows= img.shape[0]
cols=img.shape[1]
resolution=rows*cols#resolution of the image
within_class_variance=np.zeros([1,piksel_values.shape[1]])

#The following loop calculates the weight,mean and variance for background and foreground.
#Each pixel value from 0 to 255 is considered as threshold value.
#T represents the threshold value from 0 to 255.
for T in range(0,256):
    total=total1=total2=total3=total4=total5=weightBg=meanBg=varianceBg=weightFg=meanFg=varianceFg=0
    for i in range(0,T):
        total=total+histr[0,i]
    weightBg=total/resolution
    for i in range(0,T):
        total1=total1+(piksel_values[0,i]*histr[0,i])
    if total==0:
        meanBg=0
    else:
        meanBg=total1/total
    for i in range(0,T):
        total2=total2+(math.pow((piksel_values[0,i]-meanBg),2)*histr[0,i])
    if total==0:
        varianceBg=0
    else:
        varianceBg=total2/total
    for i in range(T,piksel_values.shape[1]):
        total3=total3+histr[0,i]
    weightFg=total3/resolution
    for i in range(T,piksel_values.shape[1]):
        total4=total4+(piksel_values[0,i]*histr[0,i])
    meanFg=total4/total3
    for i in range(T,piksel_values.shape[1]):
        total5=total5+(math.pow((piksel_values[0,i]-meanFg),2)*histr[0,i])
    varianceFg=total5/total3
    within_class_variance[0,T]=(weightBg*varianceBg)+(weightFg*varianceFg)

#The following loop finds the minimum value of within class variance
minimum_value=1000
for j in range(0,within_class_variance.shape[1]):
    if(within_class_variance[0,j]<minimum_value):
        minimum_value=within_class_variance[0,j]
        
#The following loop finds the optimum threshold value based on the minimum value of the within-class variance.
for k in range(0,within_class_variance.shape[1]):
    if(minimum_value==within_class_variance[0,k]):
        threshold_value=k
        print("Threshold value:",threshold_value)
        break
for i in range(0,rows):
    for j in range(0,cols):
        if img[i,j]<threshold_value:
            img[i,j]=0
        else:
            img[i,j]=255
cv2.imshow("thresh",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
