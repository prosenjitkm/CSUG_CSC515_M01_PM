# Colorado State University Global

# CSUG CSC525 Machine Learning: Module 1 Portfolio Milestone

---

**Summary:**
For my Module 1 Portfolio Milestone in the Colorado State University Global CSC525 Machine Learning course, I developed a robust Python application using OpenCV that allows users to load, display, and save copies of images with ease. The application is designed to be user-friendly and handles a wide range of scenarios, including missing files, custom input/output locations, and automatic filename incrementing to prevent overwriting. To use the application, simply run the provided `main.py` file (it works as a standalone script), follow the on-screen prompts to select your image and output directory, and the program will display the image and save a uniquely named copy in your chosen location. This tool is ideal for anyone needing a reliable way to process and organize images as part of their computer vision learning or portfolio work.

---

## Project Overview
This project is for the Module 1 Portfolio Milestone in the CSUG course Machine Learning (CSC525), Spring 2026, 8 Week Session A. It demonstrates basic OpenCV usage in Python for image loading, displaying, and saving, as required by the assignment.

You will:
- Install OpenCV and numpy (if not already installed)
- Use Python to load an image (default: `numbers_image.jpg` in a `resources` folder)
- Display the image in a window
- Save a copy of the image to a directory, with automatic filename incrementing to avoid overwriting
- Handle all user input scenarios robustly

This project meets the requirements for **Option #2: Installing OpenCV 2** (numbers image), but can be adapted for Option #1 (brain image) by changing the default image.

---

## How to Use

1. **Install dependencies** (in your project folder):
   ```bash
   pip install opencv-python numpy
   ```

2. **Prepare your image:**
   - By default, the script looks for `resources/numbers_image.jpg`.
   - You can use any image by providing its path when prompted.

3. **Run the script:**
   ```bash
   python main.py
   ```

4. **Follow the prompts:**
   - Press Enter to use the default image and directory (if available), or provide a custom path.
   - If you provide a directory, you will be prompted for the file name.
   - The script will display the image and save a copy in the chosen directory.

---

## Edge Cases & Scenarios Handled

- **No `resources` folder:**
  - The script will print an error and prompt you to provide a valid image path.
- **No default image in `resources`:**
  - The script will print an error and prompt you to provide a valid image path.
- **User provides a directory instead of a file:**
  - The script will prompt for the file name in that directory.
- **User provides a file path that does not exist:**
  - If the parent directory exists, the script will prompt for the file name in that directory.
  - If the parent directory does not exist, the script will prompt again for a valid path.
- **User provides a file path for output directory:**
  - The script will use the directory part of the path.
- **Output directory does not exist:**
  - The script will create it automatically.
- **Image cannot be loaded (corrupt or wrong format):**
  - The script will prompt again for a valid image file.
- **Output file naming:**
  - The script will never overwrite an existing file. It scans the output directory for files matching the pattern `<input_base>_copy_N.png` and saves the new copy as the next available number.
  - If you use a file that already has `_copy_N` in its name, the script will append another `_copy_M` as needed (e.g., `abcd_copy_2_copy_1.png`).
- **All user input is validated:**
  - The script will keep prompting until valid paths and files are provided.

---

## Example Usage

- **Default (resources/numbers_image.jpg):**
  ```
  Enter the path of the image to process (press Enter for default: resources/numbers_image.jpg): [press Enter]
  Enter the directory to save the copy (press Enter for default: resources): [press Enter]
  Image saved as: resources/numbers_image_copy_1.png
  ```
- **Custom image and output directory:**
  ```
  Enter the path of the image to process (press Enter for default: resources/numbers_image.jpg): C:/Users/you/Pictures
  Enter the file name in 'C:/Users/you/Pictures': myphoto.jpg
  Enter the directory to save the copy (press Enter for default: C:/Users/you/Pictures): C:/Users/you/Desktop
  Image saved as: C:/Users/you/Desktop/myphoto_copy_1.png
  ```
- **If you provide a file path that does not exist:**
  ```
  Enter the path of the image to process (press Enter for default: resources/numbers_image.jpg): C:/Users/you/Pictures/doesnotexist.jpg
  'C:/Users/you/Pictures/doesnotexist.jpg' does not exist as a file. Assuming 'C:/Users/you/Pictures' is a directory.
  Enter the file name in 'C:/Users/you/Pictures': myphoto.jpg
  ...
  ```

---

## Authors / Developers

Prosenjit Kumar Mandal
Masters Student in Artificial Intelligence and Machine Learning
Colorado State University Global
Email: prosenjitkm91@gmail.com
LinkedIn: [www.linkedin.com/in/prosenjitkm](https://www.linkedin.com/in/prosenjitkm)
