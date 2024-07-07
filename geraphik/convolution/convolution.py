from PIL import Image 
import numpy as np
import numpy as np
from PIL import Image

def convolve(image, kernel):
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape

 
    output_height = image_height - kernel_height + 1
    output_width = image_width - kernel_width + 1

   
    output = np.zeros((output_height, output_width))


    for i in range(output_height):
        for j in range(output_width):
            region = image[i:i+kernel_height, j:j+kernel_width]
            output[i, j] = np.sum(region * kernel)

    return output


image = Image.open('/home/moradi/other/university/university/geraphik/convolution/image.jpg').convert('L')
image_array = np.array(image)


filter1 = np.array([[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]])

filter2 = np.array([[-1, -1,-1],
                    [-1, 8, -1],
                    [-1, -1, -1]])

filter3 = np.array([[0, -1, 0],
                    [-1, 5, -1],
                    [0, -1, 0]])


filtered_image1 = convolve(image_array, filter1)
filtered_image2 = convolve(image_array, filter2)
filtered_image3 = convolve(image_array, filter3)


filtered_image1 = np.clip(filtered_image1, 0, 255).astype(np.uint8)
filtered_image2 = np.clip(filtered_image2, 0, 255).astype(np.uint8)
filtered_image3 = np.clip(filtered_image3, 0, 255).astype(np.uint8)


filtered_image1 = Image.fromarray(filtered_image1, mode='L')
filtered_image2 = Image.fromarray(filtered_image2, mode='L')
filtered_image3 = Image.fromarray(filtered_image3, mode='L')


filtered_image1.save('filtered_image1.jpg')
filtered_image2.save('filtered_image2.jpg')
filtered_image3.save('filtered_image3.jpg')
