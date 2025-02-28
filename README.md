Overall Purpose of the Program: The purpose of this program is to apply mathematical transformations to an image’s pixel data to create unique visual effects. The user can choose from three different filters: a color swap filter, a contrast adjustment filter, and a gamma correction filter. The program allows customization by taking user input for the contrast and gamma correction filters. The processed image is then saved to a user-specified file.
Note: The code uses Python Pillow Library installed using 
pip3 install --upgrade pillow for ( for PIL import Image) to read a jpeg image.

Program Input and Output:
Input: The program prompts the user for an image file path (JPEG format), asks them to choose one of the three filters, and allows customization for the contrast and gamma correction filters. The user also provides the output file name.
Output: The transformed image is saved to the specified file location with the selected filter applied.
First Code Segment (Storing Data in a List):
pixels = list(image.getdata())
Description: This line reads all pixel data from the image and stores it in the pixels list, where each element represents an (R, G, B) tuple.
Second Code Segment (Using the List for Processing):
transformed_pixels = []
for r, g, b in pixels:
    transformed_pixels.append(((g + 30) % 256, (b + 20) % 256, (r - 15) % 256))
image.putdata(transformed_pixels)
Description: This segment iterates through the pixels list, applies a transformation to each RGB value, and stores the modified pixels in transformed_pixels. Finally, it updates the image with the new pixel data.
Name and Purpose of the List:
List Name: pixels
Purpose: This list represents the RGB pixel data of the image and is used for applying transformations at the pixel level.
How the List Manages Complexity: The pixels list simplifies image processing by allowing direct access and iteration over pixel data. Without a list, the program would have to process each pixel individually using function calls, making the code significantly more complex and inefficient. Using a list enables batch processing of all pixels, reducing computational overhead and improving performance.

