import cv2
import mss
import pyautogui
import numpy as np
from PIL import ImageGrab

# left_branch_bbox = (300, 460, 600, 600)
# right_branch_bbox = (500, 460, 800, 600)

# branchLeft = cv2.imread('./pictures/cannyLeftBranch.jpg', cv2.IMREAD_UNCHANGED)
# branchRight = cv2.imread('./pictures/cannyRightBranch.jpg', cv2.IMREAD_UNCHANGED)

# cv2.imshow('left', branchLeft)
# cv2.imshow('right', branchRight)


# # --------------------------------------------------------------------------------------

# method = cv2.TM_SQDIFF_NORMED

# result = cv2.matchTemplate(cannyEdgesBranchLeft, large_image, method)

# # We want the minimum squared difference
# mn,_,mnLoc,_ = cv2.minMaxLoc(result)

# # Draw the rectangle:
# # Extract the coordinates of our best match
# MPx,MPy = mnLoc

# # Step 2: Get the size of the template. This is the same size as the match.
# trows,tcols = cannyEdgesBranchLeft.shape[:2]

# # Step 3: Draw the rectangle on large_image
# cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

# # Display the original image with the rectangle around the match.
# cv2.imshow('output',large_image)

# # --------------------------------------------------------------------------------------

# # while True:
# img = ImageGrab.grab(bbox=) #x, y, w, h
# img_np = np.array(img)
# frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
# cv2.imshow("frame", frame)
# # if cv2.waitKey(1) & 0Xff == ord('q'):
#     # break

# i need to find position of buttons to click
# make a function for image searching - generic
# make a function for mouse clicks - generic
    
cv2.waitKey(0)
cv2.destroyAllWindows()
