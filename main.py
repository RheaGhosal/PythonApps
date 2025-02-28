from PIL import Image


def load_image(image_path):
    """Load an image and convert it to RGB mode."""
    img = Image.open(image_path).convert("RGB")
    return img


def save_image(img, output_path):
    """Save the processed image."""
    img.save(output_path)

# Three filters below with non trivial mathematical computations e.g using mod
def color_swap_filter(image):
    """Apply a non-trivial color swap by shifting RGB channels and applying a transformation."""
    pixels = list(image.getdata())
    transformed_pixels = []

    for r, g, b in pixels:
        transformed_pixels.append(((g + 30) % 256, (b + 20) % 256, (r - 15) % 256))

    image.putdata(transformed_pixels)
    return image


def contrast_filter(image, factor):
    """Enhance contrast by applying a contrast factor to each pixel."""
    pixels = list(image.getdata())
    avg = tuple(sum(x) // len(pixels) for x in zip(*pixels))
    transformed_pixels = []

    for r, g, b in pixels:
        transformed_pixels.append((
            int(avg[0] + ((r - avg[0]) % factor)),
            int(avg[1] + ((g - avg[1]) % factor)),
            int(avg[2] + ((b - avg[2]) % factor))
        ))

    image.putdata(transformed_pixels)
    return image


def gamma_correction(image, gamma):
    """Apply gamma correction to adjust brightness and contrast non-linearly."""
    pixels = list(image.getdata())
    transformed_pixels = []

    for r, g, b in pixels:
        transformed_pixels.append((
            int((r / 255) ** gamma * 255) % 256,
            int((g / 255) ** gamma * 255) % 256,
            int((b / 255) ** gamma * 255) % 256
        ))

    image.putdata(transformed_pixels)
    return image


def main():
    image_path = input("Enter the path of the image file: ")
    img = load_image(image_path)

    while True:
        print("\nChoose a filter:")
        print("1. Color Swap Filter")
        print("2. Contrast Adjustment (User Input Required)")  # First filter requiring user input
        print("3. Gamma Correction (User Input Required)")  # Second filter requiring user input
        print("4. Exit")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            filtered_img = color_swap_filter(img)
            #  contrast_filter  incorporate user input  'factor' into the code to create the filter
        elif choice == 2:
            factor = float(input(
                "Enter contrast factor (e.g., 1.5 for high contrast, 0.5 for low contrast): "))  # User input required
            filtered_img = contrast_filter(img, factor)
            #  gamma_correction  incorporate user input  'gamma' into the code to create the filter
        elif choice == 3:
            gamma = float(
                input("Enter gamma value (e.g., 2.0 for brightening, 0.5 for darkening): "))  # User input required
            filtered_img = gamma_correction(img, gamma)
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

        output_path = input("Enter the output image filename: ")
        save_image(filtered_img, output_path)
        print(f"Filtered image saved as {output_path}")


if __name__ == "__main__":
    main()
