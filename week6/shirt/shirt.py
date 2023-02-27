# Import libraries
import sys
from PIL import Image, ImageOps


def main():
    # Check the CL arguments
    check_cl_args()
    # Openning input image
    try:
        input_image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    # Storing size of shirt.png
    shirt_image = Image.open("shirt.png")
    size = shirt_image.size
    # Resizing the input image to fit the shirt
    resized_input = ImageOps.fit(input_image, size)
    # Pasting shirt onto the input
    resized_input.paste(shirt_image, shirt_image)
    # Saving the final_output
    resized_input.save(sys.argv[2])


def check_cl_args():
    # Check for the 2 CL arg
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    # Check file types & store file extensions
    valid_file_types = [".jpg", ".jpeg", ".png"]
    extension_found_arg1 = False
    extension_found_arg2 = False
    arg1_extension = ""
    arg2_extension = ""

    for extension in valid_file_types:
        if sys.argv[1].lower().endswith(extension):
            extension_found_arg1 = True
            arg1_extension = extension
        if sys.argv[2].lower().endswith(extension):
            extension_found_arg2 = True
            arg2_extension = extension
    if not extension_found_arg1 or not extension_found_arg2:
        sys.exit("Arguments need to be image files")

    # Check for matching extensions
    if not arg1_extension == arg2_extension:
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
