

# File Name : movie_Decryptor.py
# Student Name: Jacob Farrell, Asfia Siddiqui
# email:  farrelcj@mail.uc.edu, siddiqaf@mail.uc.edu
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
#   Handles the movie title decryption task. Contains a function 
#   (`get_encrypted_movie_message`) to read the TeamsAndEncryptedMessages JSON file
#   and extract the encrypted string for a specific team. Also contains the main 
#   decryption function (`decrypt_movie_message`) which uses the cryptography.fernet
#   library and a provided key (from config) to decrypt the message.
# Citations: {List any websites, books, or specific resources used}
#   - Google Gemini (generative AI assistant): Assistance with code structure, 
#     debugging, function implementation, docstrings, and explaining concepts. 
#     URL: https://gemini.google.com/ 

# Anything else that's relevant: {Add any notes if applicable}
import json
import os
from cryptography.fernet import Fernet, InvalidToken

def get_encrypted_movie_message(messages_filepath, team_name):
    """
    Reads the JSON dictionary file and returns the encrypted message STRING for the team.
    Handles the case where the message is stored in a list in the JSON.
    
    @param messages_filepath (str): Path to the JSON file containing encrypted messages.
    @param team_name (str): The name of the team to look up.
    @return (str or None): The encrypted message string, or None if not found/error.
    """
    if not os.path.exists(messages_filepath):
        print(f"Error: Movie messages file not found at '{messages_filepath}'")
        return None
        
    try:
        with open(messages_filepath, 'r', encoding='utf-8') as f:
            all_messages = json.load(f)

        message_data = all_messages.get(team_name)

        if message_data and isinstance(message_data, list) and len(message_data) > 0:
            encrypted_string = message_data[0] 
            if isinstance(encrypted_string, str):
                 print(f"Found encrypted message string for team '{team_name}'")
                 return encrypted_string
            else:
                 print(f"Warning: Found data for team '{team_name}', but the first element in the list was not a string.")
                 return None
        elif message_data:
             print(f"Warning: Data format for team '{team_name}' in {os.path.basename(messages_filepath)} is unexpected (expected non-empty list).")
             return None
        else:
            print(f"Warning: Team '{team_name}' not found as a key in {os.path.basename(messages_filepath)}")
            return None 

    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {os.path.basename(messages_filepath)}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred reading movie messages file: {e}")
        return None


def decrypt_movie_message(encrypted_message, key):
    """
    Decrypts the Fernet encrypted message using the provided key.

    @param encrypted_message (str): The base64 encoded encrypted message string.
    @param key (bytes or str): The Fernet decryption key. Should ideally be bytes.
    @return (str): The decrypted message string, or an error message string.
    """
    if not encrypted_message:
        return "Error: No encrypted message provided for movie decryption."
    if key is None:
        return "Error: Movie decryption key is missing. Obtain it from your instructor and update config.py."
    if not isinstance(key, bytes):
         print("Warning: Movie decryption key was provided as string, attempting to encode. Ensure it's the correct byte representation.")
         try:
              key = key.encode('utf-8')
         except Exception as e:
              return f"Error: Could not encode provided key string to bytes: {e}"

    try:
        if isinstance(encrypted_message, str):
            encrypted_message_bytes = encrypted_message.encode('utf-8')
        else:
            encrypted_message_bytes = encrypted_message 

        f = Fernet(key)
        decrypted_bytes = f.decrypt(encrypted_message_bytes)
        decrypted_message = decrypted_bytes.decode('utf-8')
        return decrypted_message
        
    except InvalidToken:
        return "Movie Decryption Error: Invalid Key or Corrupted Message (InvalidToken)."
    except Exception as e:
        return f"An unexpected error occurred during movie decryption: {e}"

# ================================================================
# End of File: decryption/movie.py
# ================================================================















