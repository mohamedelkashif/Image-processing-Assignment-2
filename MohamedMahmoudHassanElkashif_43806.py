import cv2
import math
import subprocess
import numpy as np

img = cv2.imread("Assignment2Input.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img3=img.copy()
score=0

kernel1=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2))
blur = cv2.GaussianBlur(gray,(3,3),0)

centercircle = blur.copy()
circles = cv2.HoughCircles(centercircle,cv2.HOUGH_GRADIENT,1,30,
                            param1=50,param2=50,minRadius=10,maxRadius=16)

# ensure at least some circles were found
if circles is  None:
    print('No circles detected follows the hough parameters')
if circles is not None:
 circles = np.uint16(np.around(circles))
 for i in circles[0,:]:
    # draw the outer circle
       cv2.circle(centercircle,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
       cv2.circle(centercircle,(i[0],i[1]),2,(0,0,255),3)
       x_cordinate_of_centered_circl=i[0]
       ycordinate_of_centered_circl=i[1]

       #print ('Number of all coinshght %d' % x)
       colorofcenter=blur[x_cordinate_of_centered_circl,ycordinate_of_centered_circl]
       print('Color of cetered circle %d' %colorofcenter )


img2 = blur.copy()





img1 = blur.copy()
circles1 = cv2.HoughCircles(img1,cv2.HOUGH_GRADIENT,2,30,
                            param1=50,param2=50,minRadius=10,maxRadius=18)
circles1 = np.uint16(np.around(circles1))

for j in circles1[0,:]:
    # draw the outer circle
       cv2.circle(img1,(j[0],j[1]),i[2],(0,255,0),2)

    # draw the center of the circle
       cv2.circle(img1,(j[0],j[1]),2,(0,0,255),3)
       x_cordinate_of_bullet = j[0]
       y_cordinate_of_bullet = j[1]
       print('Radii of bullet circles %d' % j[2])
       print('X coordinate of bullets %d' % j[0])
       print('Y coordinates of bullet %d' % j[1])
       colorofbullet=blur[x_cordinate_of_bullet,y_cordinate_of_bullet]
       print('Color of bullet circle %d' %colorofbullet )







       if math.sqrt(math.pow((j[0] - 237),2) + math.pow((j[1] - 245),2)) <16 and math.sqrt(math.pow((j[0] - 237),2) + math.pow((j[1] - 245),2)) !=0:
           score+=9
       elif math.sqrt(math.pow((j[0] - 237),2) + math.pow((j[1] - 245),2)) <33 and math.sqrt(math.pow((j[0] - 237),2) + math.pow((j[1] - 245),2)) !=0:
           score+=8
           #print('8')
       elif math.sqrt(math.pow((j[0] - 237),2) + math.pow((j[1] - 245),2)) <80 and math.sqrt(math.pow((j[0] - 237),2) + math.pow((j[1] - 245),2)) !=0:
           score+=7
           #print('7')
       elif math.sqrt(math.pow((j[0] - 237),2) + math.pow((j[1] - 245),2)) <128 and math.sqrt(math.pow((j[0] - 237),2) + math.pow((j[1] - 245),2)) !=0:
           score+=6
           #print('6')

       elif math.sqrt(math.pow((j[0] - 237),2) + math.pow((j[1] - 245),2)) <175 and math.sqrt(math.pow((j[0] - 237),2) + math.pow((j[1] - 245),2)) !=0:
           score+=5
           #print('5')
       elif math.sqrt(math.pow((j[0] - 237),2) + math.pow((j[1] - 245),2)) <222 and math.sqrt(math.pow((j[0] - 237),2) + math.pow((j[1] - 245),2)) !=0:
           score+=4
           #print('4')
       elif math.sqrt(math.pow((j[0] - 237),2) + math.pow((j[1] - 245),2)) <286 and math.sqrt(math.pow((j[0] - 237),2) + math.pow((j[1] - 245),2)) !=0:
           score+=3
           #print('3')


print(score)
img3=img.copy()
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img3,'Score = %d'%score,(220,50), font, 1,(255,0,0),2)
cv2.circle(img3,(238,246),16,(0,255,0),2)
cv2.circle(img3,(238,246),33,(0,255,0),2)
cv2.circle(img3,(238,246),80,(0,255,0),2)
cv2.circle(img3,(238,246),128,(0,255,0),2)
cv2.circle(img3,(238,246),175,(0,255,0),2)
cv2.circle(img3,(238,246),222,(0,255,0),2)
cv2.circle(img3,(238,246),268,(0,255,0),2)
cv2.circle(img3,(125,261),13,(0,0,255),2)
cv2.circle(img3,(91,257),13,(0,0,255),2)
cv2.circle(img3,(149,323),j[2],(0,0,255),2)
cv2.circle(img3,(129,207),j[2],(0,0,255),2)
cv2.circle(img3,(113,431),j[2],(0,0,255),2)

cv2.circle(img2,(238,246),16,(0,255,0),2)
cv2.circle(img2,(238,246),33,(0,255,0),2)
cv2.circle(img2,(238,246),80,(0,255,0),2)
cv2.circle(img2,(238,246),128,(0,255,0),2)
cv2.circle(img2,(238,246),175,(0,255,0),2)
cv2.circle(img2,(238,246),222,(0,255,0),2)
cv2.circle(img2,(238,246),268,(0,255,0),2)
cv2.imshow('Final image',img3)
cv2.imshow('Detected Rings',img2)
cv2.imshow('Detected bullets',img1)
cv2.imshow('detected center circle',centercircle)
cv2.imshow('After Gussian filter to remove noise',blur)
cv2.imshow('After rgb2gray',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('MohamedMahmoudHassanElkashif_43806_Finalimage.png',img3)
cv2.imwrite('MohamedMahmoudHassanElkashif_43806_Detected Rings.png',img2)
cv2.imwrite('MohamedMahmoudHassanElkashif_43806_Detected bullets.png',img1)
cv2.imwrite('MohamedMahmoudHassanElkashif_43806_detected center circle.png',centercircle)
cv2.imwrite('MohamedMahmoudHassanElkashif_43806_After Gussian filter to remove noise.png',blur)
cv2.imwrite('MohamedMahmoudHassanElkashif_43806_After rgb2gray.png',gray)
