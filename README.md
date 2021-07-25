# Real-time-Object-dimension-Detection
Finding the dimensions of the given object

The code flow will be like this

• Import all the libraries required
• Finding the pixel per metric ratio
• Open the camera, convert into grayscale and blur it slightly
• Perform edge detection, then perform a dilation and erosion to close the gaps between the object edges
• Find the contours that corresponds to objects and pick the contour with maximum area
• The contour with maximum area is our object whose dimensions has to be found
• Compute the bounding box of the contour and draw the outline of bounding box
• Compute the size of the object by using pixel per metric ratio and put them on the screen

For this code the user must enter a parameter (the distance between the camera and object)
