import cv2  as cv 

# img =   cv.imread('C:/Users/Hemanth2512005/Desktop/OpenCV/Images/elephant.jpg ')
img =   cv.imread('C:/Users/Hemanth2512005/Desktop/OpenCV/Images/wallpaper.jpg')

if img is None:
    print("Failed to load image.")
    exit()
 

def  rescaleFrame(frame , scale = 0.75 ):
    width =  frame.shape[1] *scale 
    height  = frame.shape[0] * scale
    dimensions = (width, height)

    # float --> int
    return cv.resize(frame,dimensions , interpolation=cv.INTER_AREA)



# Function to rescale image
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Rescale the image
rescaled_img = rescaleFrame(img)

# Show the image
cv.imshow('Rescaled Wallpaper', rescaled_img)

# Wait indefinitely until a key is pressed
cv.waitKey(0)
cv.destroyAllWindows()