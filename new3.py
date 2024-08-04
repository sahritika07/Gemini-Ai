import cv2

# Load an image from file
image = cv2.imread('img3.jpg')
cv2.imshow("Image", image)
# Check if the image was loaded successfully
if image is None:
    print("Error loading image")
else:
    # Display the image in a window named 'Image'
    cv2.imshow('Image', image)

    # Wait indefinitely for a key event
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
