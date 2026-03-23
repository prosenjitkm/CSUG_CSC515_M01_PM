import numpy as np
import cv2
import os
import re

# -----------------------------
# Configuration and Defaults
# -----------------------------
resources_dir = 'resources'  # Default directory for resources
default_input_filename = 'numbers_image.jpg'  # Default image file name
# Full default path to the input image
default_input_path = os.path.join(resources_dir, default_input_filename)
# Default output directory (same as resources)
default_output_dir = resources_dir


def check_default_available():
    """
    Check if the default resources directory and default image exist.
    Returns True if both exist, False otherwise.
    """
    if not os.path.isdir(resources_dir):
        print(f"Error: Default directory '{resources_dir}' does not exist.")
        return False
    if not os.path.isfile(default_input_path):
        print(f"Error: Default image '{default_input_path}' does not exist.")
        return False
    return True


def get_input_file_path():
    """
    Prompt the user for the image file path to process.
    Handles the following cases:
    - User presses Enter: use default path
    - User provides a directory: prompt for file name
    - User provides a file path: use if valid, else prompt for file name in parent directory
    Returns the full path to the image file.
    """
    while True:
        user_path = input(f"Enter the path of the image to process (press Enter for default: {default_input_path}): ").strip()
        if user_path == '':
            # Use default
            return default_input_path
        user_path = os.path.expanduser(user_path)
        if os.path.isdir(user_path):
            # User gave a directory, prompt for file name
            file_name = input(f"Enter the file name in '{user_path}': ").strip()
            candidate = os.path.join(user_path, file_name)
            if os.path.isfile(candidate):
                return candidate
            else:
                print(f"Error: File '{candidate}' does not exist.")
                continue
        elif os.path.isfile(user_path):
            # User gave a valid file path
            return user_path
        else:
            # Path does not exist as file, check if parent is a directory
            parent = os.path.dirname(user_path)
            if os.path.isdir(parent):
                print(f"'{user_path}' does not exist as a file. Assuming '{parent}' is a directory.")
                file_name = input(f"Enter the file name in '{parent}': ").strip()
                candidate = os.path.join(parent, file_name)
                if os.path.isfile(candidate):
                    return candidate
                else:
                    print(f"Error: File '{candidate}' does not exist.")
                    continue
            else:
                print(f"Error: '{user_path}' is not a valid file or directory.")
                continue


def get_output_dir(default_dir):
    """
    Prompt the user for the output directory.
    If the user provides a file path, use its directory.
    If the user presses Enter, use the default directory.
    Ensures the output directory exists (creates if needed).
    Returns the output directory path.
    """
    while True:
        user_path = input(f"Enter the directory to save the copy (press Enter for default: {default_dir}): ").strip()
        if user_path == '':
            output_dir = default_dir
        else:
            user_path = os.path.expanduser(user_path)
            # If user gives a file path, use its directory
            if os.path.isdir(user_path):
                output_dir = user_path
            else:
                output_dir = os.path.dirname(user_path) or '.'
        try:
            os.makedirs(output_dir, exist_ok=True)
            return output_dir
        except Exception as e:
            print(f"Error: Could not create or access directory '{output_dir}': {e}")


# -----------------------------
# Main Program Flow
# -----------------------------

# Step 1: Check if defaults are available (resources folder and default image)
if check_default_available():
    # If defaults exist, allow user to use them or provide custom path
    input_path = get_input_file_path()
else:
    # If defaults are missing, require user to provide a valid image path
    print("Default image and/or directory not available. Please provide a path to the image file.")
    input_path = get_input_file_path()

# Step 2: Determine the output directory
# By default, output is saved in the same directory as the input file
input_dir = os.path.dirname(input_path) or '.'
default_output_dir = input_dir
output_dir = get_output_dir(default_output_dir)

# Step 3: Load the image, re-prompt if not found or unreadable
img = cv2.imread(input_path)
while img is None:
    print(f"Error: Could not load '{input_path}'. Make sure the file exists and the path is correct.")
    input_path = get_input_file_path()
    input_dir = os.path.dirname(input_path) or '.'
    default_output_dir = input_dir
    output_dir = get_output_dir(default_output_dir)
    img = cv2.imread(input_path)

# Step 4: Generate the output file name using the input file's base name
# The output file will be named <input_base>_copy_<N>.png, where N is incremented
input_base = os.path.splitext(os.path.basename(input_path))[0]
pattern = re.compile(re.escape(input_base) + r'_copy_(\d+)\.png$')
existing = [f for f in os.listdir(output_dir) if pattern.match(f)]
if existing:
    nums = [int(pattern.match(f).group(1)) for f in existing]
    next_num = max(nums) + 1
else:
    next_num = 1
output_filename = f'{input_base}_copy_{next_num}.png'
output_path = os.path.join(output_dir, output_filename)

# Step 5: Save the image copy to the output directory
cv2.imwrite(output_path, img)

# Step 6: Display the image in a window
cv2.imshow('numbers_window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 7: Inform the user where the image was saved
print(f"Image saved as: {output_path}")
