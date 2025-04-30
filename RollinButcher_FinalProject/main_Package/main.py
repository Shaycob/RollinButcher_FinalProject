# File Name : main.py
# Student Name: Jacob Farrell
# email:  farrelcj@mail.uc.edu
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
#   Serves as the main entry point and orchestrator for the IS4010 Final Project 
#   application. It imports necessary configuration and functions from other 
#   packages (`decryption`, `display`), executes the location and movie decryption 
#   steps, attempts to process and initiate the display of the team photo, prints 
#   status messages and results to the console, and pauses execution at the end.
# Citations: {List any websites, books, or specific resources used}
#   - Google Gemini (generative AI assistant): Assistance with code structure, 
#     debugging, function implementation, docstrings, and explaining concepts. 
#     URL: https://gemini.google.com/ 

# Anything else that's relevant: {Add any notes if applicable}
import sys
import os
import webbrowser 

try:
    import config 
    print("Configuration loaded from config.py")
except ImportError:
    print("Warning: config.py not found in main_Package. Using default values defined in main.py.")
    # Define defaults directly if config.py is not found
    # This makes main.py runnable even without config.py, but less flexible
    class DefaultConfig:
        TEAM_NAME = "Rollin Butcher" # Default team name
        # Calculate paths assuming main.py is in main_Package
        MAIN_PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
        PROJECT_ROOT = os.path.dirname(MAIN_PACKAGE_DIR)
        DATA_DIR = os.path.join(PROJECT_ROOT, "data_Package") # Assumes data_Package is parallel to main_Package
        
        # Construct full paths using the determined DATA_DIR
        LOCATION_HINTS_FILE = os.path.join(DATA_DIR, "EncryptedGroupHintsSpring2025.json") # Check filename if needed
        MOVIE_MESSAGES_FILE = os.path.join(DATA_DIR, "TeamsAndEncryptedMessagesForDistribution.json")
        DICTIONARY_FILE = os.path.join(DATA_DIR, "UCEnglish.txt")
        # Default key is None - MUST be replaced if config.py is not used
        MOVIE_DECRYPTION_KEY = None 
        TEAM_PHOTO_FILE = os.path.join(DATA_DIR, "team_photo.jpg") # Default photo name
    config = DefaultConfig()


# --- Import project functions ---
# (Keep the sys.path modification and imports as before)
PROJECT_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT_PATH not in sys.path:
    sys.path.insert(0, PROJECT_ROOT_PATH)
try:
    from decryptor_Package.location_Decryptor import get_location_indices, decrypt_location_from_indices
    from decryptor_Package.movie_Decryptor import get_encrypted_movie_message, decrypt_movie_message
    from display_Package.image_Display import process_and_save_photo 
except ImportError as e:
     print(f"\nCRITICAL ERROR importing project modules: {e}")
     # ... (rest of import error handling) ...
     sys.exit(1) 


# --- Main Execution Function ---
def run_final_project():
    """
    Runs the sequence of tasks for the final project:
    1. Decrypts location from hints file and dictionary.
    2. Decrypts movie title from messages file using a key from config.
    3. Processes and displays the team photo via the default browser/viewer.
    4. Prints a summary of results.
    Pauses at the end for user review.
    
    @param: None
    @return: None
    """
    print(f"\n--- Running Final Project for Team: {config.TEAM_NAME} ---")
    
    decrypted_location = "[ERROR: Processing Failed]" 
    decrypted_movie = "[ERROR: Processing Failed]"    
    photo_opened = False        

    # 1. Decrypt Location
    print("\nStep 1: Decrypting Location...")
    try:
        location_indices = get_location_indices(config.LOCATION_HINTS_FILE, config.TEAM_NAME)
        if location_indices:
            decrypted_location = decrypt_location_from_indices(location_indices, config.DICTIONARY_FILE)
            print(f"--> Decrypted Location: {decrypted_location}")
        else:
            decrypted_location = "[ERROR: Indices not found]"
    except Exception as e:
        print(f"An unexpected error occurred during location processing: {e}")
        decrypted_location = f"[ERROR: {e}]"


    # 2. Decrypt Movie
    print("\nStep 2: Decrypting Movie Title...")
    try:
        encrypted_movie = get_encrypted_movie_message(config.MOVIE_MESSAGES_FILE, config.TEAM_NAME)
        if encrypted_movie:
            decrypted_movie = decrypt_movie_message(encrypted_movie, config.MOVIE_DECRYPTION_KEY) 
            print(f"--> Decrypted Movie: {decrypted_movie}")
            if "Error:" in decrypted_movie:
                 print("Note: Movie decryption failed. Ensure the MOVIE_DECRYPTION_KEY in config.py is correct and obtained from your instructor.")
        else:
            decrypted_movie = "[ERROR: Encrypted message not found]"
    except Exception as e:
         print(f"An unexpected error occurred during movie processing: {e}")
         decrypted_movie = f"[ERROR: {e}]"
         
    # 3. Process and Open Photo
    print("\nStep 3: Processing and Opening Team Photo...")
    print(f"(Looking for photo at: {config.TEAM_PHOTO_FILE})")
    try:
        saved_photo_path = process_and_save_photo(config.TEAM_PHOTO_FILE)
        
        if saved_photo_path:
            try:
                file_uri = f"file:///{os.path.abspath(saved_photo_path).replace(os.path.sep, '/')}" 
                print(f"Attempting to open saved image via webbrowser: {file_uri}")
                webbrowser.open(file_uri)
                photo_opened = True
                print("--> Photo opening initiated (check your browser or default image viewer).")
            except Exception as wb_e:
                print(f"Error opening image with webbrowser: {wb_e}")
                photo_opened = False
        else:
             print("Photo processing/saving failed.")
             photo_opened = False
             
    except Exception as e:
        print(f"An unexpected error occurred during photo processing/opening step: {e}")
        photo_opened = False


    # --- Final Summary ---
    print("\n--- Project Execution Summary ---")
    print(f"Team: {config.TEAM_NAME}")
    print(f"Location: {decrypted_location}")
    print(f"Movie: {decrypted_movie}")
    if not photo_opened: print("Photo Status: Display failed or file not found/processed")
    else: print("Photo Status: Display initiated successfully")
    print("--- End of Summary ---")


# --- Script Entry Point ---
if __name__ == "__main__":
    run_final_project()

