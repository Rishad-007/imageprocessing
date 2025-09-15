# Simple version for displayimage.py
import cv2
import matplotlib.pyplot as plt

# Load color image
color_img = cv2.imread("input/Rishad-pic.jpg")
color_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB

# Convert to grayscale
gray_img = cv2.cvtColor(color_img, cv2.COLOR_RGB2GRAY)

# Display both images side by side
plt.figure(figsize=(10, 4))

# Color image
plt.subplot(1, 2, 1)
plt.imshow(color_img)
plt.title("Color Image")
plt.axis('off')

# Grayscale image
plt.subplot(1, 2, 2)
plt.imshow(gray_img, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')

plt.show()

# Print basic information
print("Color image shape:", color_img.shape)  # (height, width, channels)
print("Grayscale image shape:", gray_img.shape)  # (height, width)
