# Otsu Thresholding Method
Nobuyuki Otsu proposed an approach in 1979 that finds the optimum threshold value of an image.
This approach determines the optimum threshold value by taking into account the changes between the foreground and background classes. 
In this approach, the histogram values of the gray pixel values are calculated in the first step.
Then, all pixel values from 0 to 255 are considered as the threshold value. 
Pixel values less than this threshold value are defined as the background and greater values are defined as the foreground.
<br><br>
weightBg,meanBg and varianceBg are calculated for the background respectively. Likewise, weightFg, meanFg ve varianceFg are calculated for the foreground respectively. 
The equations of these values are shown below;
<br><br>
![GitHub Logo](/images/equation1.jpg)
<br><br>
Within class variance is calculated using the values shown above.
The equation of the within class variance is given by;
<br><br>
![GitHub Logo](/images/equation2.jpg)
<br><br>
All values from 0 to 255 are considered threshold value and then the within-class variance is calculated using equation 7.
The pixel value with the least within-class variance value is determined as the threshold value.
<br><br>
### Original Image:
![GitHub Logo](/images/animal.jpg)
<br><br>
### Output:
The threshold value was calculated as 163 by using otsu.py<br>
![GitHub Logo](/images/animal_binary.jpg)
