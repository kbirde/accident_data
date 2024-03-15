import sys
from PIL import Image
import os

def display_image(image_path):
    try:
        # Open the image file
        img = Image.open(image_path)

        # Display the image
        img.show()
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python state_codes_image.py <image_path>")
        sys.exit(1)

    # Get the image path from the command-line argument
    image_path = sys.argv[1]

    # Check if the image file exists
    if os.path.exists(image_path):
        # Display the image
        display_image(image_path)
    else:
        print("Image file not found at the specified path:", image_path)
