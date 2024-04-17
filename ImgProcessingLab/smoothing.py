import numpy as np

#BOX FILTER
filter = np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])

#random 5x5 image
image = np.array([[1,2,3],[4,5,6,],[7,8,9]])

#convolution
def convolution(image, filter):
    
    result = np.zeros((image.shape[0]+2, image.shape[1]+2))
    
    # zero padding
    image = np.pad(image,[(2,), (2,)],mode = 'constant')
    
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            result[i,j] = np.sum(image[i:i+3, j:j+3]*filter)
            
    return result

filtered_image = convolution(image, filter)

print("\nOriginal Image : \n", image)
print("\nFiltered (Smoothened) Image : \n", filtered_image)

def sum_of_pixels(image):
    return np.sum(image)

print("\nSum of pixels in filter : ", np.sum(filter))

print("Sum of pixels in original image : ", sum_of_pixels(image))
print("Sum of pixels in filtered (Smoothened) image : ", sum_of_pixels(filtered_image))