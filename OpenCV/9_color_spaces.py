
import cv2 as cv 
import matplotlib.pyplot as plt 

img =  cv.imread('Images/roadway.jpg')
cv.imshow('Img',img) 

#matplotlib shows as rgb image  ---- not bgr 
# plt.imshow(img)
# plt.show()

#bgr to rgb 
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
# cv.imshow('rgb',rgb)

#BGR  to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

#bgr to hsv 
hsv = cv.cvtColor( img,cv.COLOR_BGR2HSV)
# cv.imshow("HSV",hsv)

#bgr to l a b
lab  = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB",lab)

#-----Note: -------- you can not  covert  gray to hsv  directly ------------> gray - bgr - hsv   <-------------------

#hsv to bgr 
hsv_bgr  = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
# cv.imshow('hsv --> bgr',hsv_bgr)

#lab to bgr 
lab_bgr= cv.cvtColor(lab,cv.COLOR_Lab2BGR)
cv.imshow('Lab--> bgr',lab_bgr)
cv.waitKey(0)



# Direct 

| From → To       | OpenCV Code          |
| --------------- | -------------------- |
| BGR → RGB       | `cv.COLOR_BGR2RGB`   |
| BGR → Grayscale | `cv.COLOR_BGR2GRAY`  |
| BGR → HSV       | `cv.COLOR_BGR2HSV`   |
| BGR → LAB       | `cv.COLOR_BGR2LAB`   |
| BGR → YCrCb     | `cv.COLOR_BGR2YCrCb` |
  
| RGB → BGR       | `cv.COLOR_RGB2BGR`   |
| RGB → Grayscale | `cv.COLOR_RGB2GRAY`  |
| RGB → HSV       | `cv.COLOR_RGB2HSV`   |

 
| Grayscale → BGR | `cv.COLOR_GRAY2BGR`  |
| Grayscale → RGB | `cv.COLOR_GRAY2RGB`  |
  
| HSV → BGR       | `cv.COLOR_HSV2BGR`   |
  
| LAB → BGR       | `cv.COLOR_LAB2BGR`   |
  
| YCrCb → BGR     | `cv.COLOR_YCrCb2BGR` |
   



#indirect 
| Invalid Conversion | Why it Fails / Fix                | What To Do Instead |
| ------------------ | --------------------------------- | ------------------ |
| Grayscale → HSV    | Missing hue/saturation info       | `GRAY → BGR → HSV` |
| Grayscale → LAB    | Missing color info                | `GRAY → BGR → LAB` |
  
| HSV → Grayscale    | Hue/saturation can’t be collapsed | `HSV → BGR → GRAY` |
| HSV → LAB          | Not directly convertible          | `HSV → BGR → LAB`  |
  
| LAB → Grayscale    | Same reason                       | `LAB → BGR → GRAY` | 
| LAB → HSV          | Not directly convertible          | `LAB → BGR → HSV`  |
