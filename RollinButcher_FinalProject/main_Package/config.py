# File Name : config.py
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
#   Stores configuration constants and settings for the IS4010 Final Project, 
#   including team name, file paths for data and dictionary files, and the 
#   Fernet decryption key (to be filled in). It also calculates absolute paths 
#   based on its own location to ensure files can be found reliably.
# Citations: {List any websites, books, or specific resources used}
#   - Google Gemini (generative AI assistant): Assistance with code structure, 
#     debugging, function implementation, docstrings, and explaining concepts. 
#     URL: https://gemini.google.com/ 

# Anything else that's relevant: {Add any notes if applicable}
import os

# --- Determine Project Root based on config.py location inside main_Package ---

# Get the directory where this config.py file is located (e.g., .../main_Package)
CONFIG_DIR = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory of CONFIG_DIR, which should be the Project Root (e.g., .../RollinButcher_FinalProject)
PROJECT_ROOT = os.path.dirname(CONFIG_DIR)
print(f"Project Root determined as: {PROJECT_ROOT}") # Debug print (Should show the path to RollinButcher_FinalProject)
print(f"Config file directory: {CONFIG_DIR}")       # Debug print (Should show the path to main_Package)

# --- TEAM NAME ---
TEAM_NAME = "Rollin Butcher" # <-- It needs to be defined here!

# --- Define paths relative to the determined PROJECT_ROOT ---
# Use the actual package name from your screenshot: "data_Package"
DATA_DIR = os.path.join(PROJECT_ROOT, "data_Package") 
print(f"Data directory targeted: {DATA_DIR}")       # Debug print

LOCATION_HINTS_FILE = os.path.join(DATA_DIR, "EncryptedGroupHintsSpring2025.json")
MOVIE_MESSAGES_FILE = os.path.join(DATA_DIR, "TeamsAndEncryptedMessagesForDistribution.json")
DICTIONARY_FILE = os.path.join(DATA_DIR, "UCEnglish.txt")
TEAM_PHOTO_FILE = os.path.join(DATA_DIR, "team_photo.jpg") # <-- Update actual photo filename if needed

# --- Decryption Key (MUST BE OBTAINED FROM INSTRUCTOR AND REPLACED) ---
# Replace None with the actual key (as a bytes object, e.g., b'key_goes_here')
MOVIE_DECRYPTION_KEY = b'DnebEey6yrDZ6OdWGf3p_wdHE8gDgfffw6UEvc4sMJg=' 
# ================================================================
# End of File: main_Package/config.py
# ================================================================

