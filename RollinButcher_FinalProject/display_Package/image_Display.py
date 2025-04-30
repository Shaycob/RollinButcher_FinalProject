# File Name : image_Display.py
# Student Name: Zoha Iqbal
# email: iqbalza@mail.uc.edu
# Assignment Number: IS4010 Final Project
# Due Date:   05/01/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Develop a collaborative Python application 
#   that decrypts location data using a dictionary file lookup, decrypts 
#   an encrypted movie title using the Fernet library (requires a key from the instructor),
#   and performs a campus scavenger hunt culminating in displaying a team photo 
#   taken at the decrypted location with a sign showing a quote from the decrypted movie.
# Brief Description of what this module does. {Do not copy/paste from a previous assignment. Put some thought into this. required}
#   Handles the processing and preparation of the team photo for display. 
#   Contains a function (`autorotate_image`) to read EXIF orientation data and 
#   rotate the image accordingly using the Pillow library. Also contains the 
#   main function (`process_and_save_photo`) which opens the original image, 
#   applies the auto-rotation, and saves a temporary copy for reliable viewing.
# Citations: {List any websites, books, or specific resources used}
#   - Google Gemini (generative AI assistant): Assistance with code structure, 
#     debugging, function implementation, docstrings, and explaining concepts. 
#     URL: https://gemini.google.com/ 

# Anything else that's relevant: {Add any notes if applicable}
from PIL import Image, ExifTags 
import os
import sys 

def autorotate_image(img):
    """
    Applies rotation based on EXIF orientation tag found in the image metadata.
    
    @param img (PIL.Image.Image): The image object loaded by Pillow.
    @return (PIL.Image.Image): The potentially rotated image object.
    """
    try:
        orientation_tag_id = -1
        for k, v in ExifTags.TAGS.items():
            if v == 'Orientation':
                orientation_tag_id = k
                break
        
        if orientation_tag_id == -1:
            return img 

        exif_data = img.getexif()
        
        if exif_data is None or orientation_tag_id not in exif_data:
            return img 

        orientation = exif_data[orientation_tag_id]
        
        if orientation == 3:
            img = img.transpose(Image.Transpose.ROTATE_180)
        elif orientation == 6:
            img = img.transpose(Image.Transpose.ROTATE_270)
        elif orientation == 8:
            img = img.transpose(Image.Transpose.ROTATE_90)
        
    except Exception as e:
        print(f"Warning: Could not process EXIF orientation data. Error: {e}")
        
    return img


def process_and_save_photo(image_filepath):
    """
    Opens the image file, applies EXIF rotation, and saves a copy 
    to a temporary location for reliable opening via webbrowser.

    @param image_filepath (str): Path to the original team photo.
    @return (str or None): The path to the saved (and possibly rotated) image file, or None if failed.
    """
    if not os.path.exists(image_filepath):
        print(f"Error: Image file not found at '{image_filepath}'")
        return None
        
    try:
        img = Image.open(image_filepath)
        print(f"Successfully opened image: {os.path.basename(image_filepath)} (Format: {img.format}, Size: {img.size}, Mode: {img.mode})")
        
        # Apply auto-rotation
        img_rotated = autorotate_image(img)
        
        # Define save path (e.g., in the project root)
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        save_path = os.path.join(project_root, "display_temp_image.jpg") 
        
        # Save the potentially rotated image
        img_rotated.save(save_path)
        print(f"Saved correctly oriented image for display to: {save_path}")
        return save_path 

    except Exception as e:
        print(f"Error opening or saving image {os.path.basename(image_filepath)}: {e}")
        return None
