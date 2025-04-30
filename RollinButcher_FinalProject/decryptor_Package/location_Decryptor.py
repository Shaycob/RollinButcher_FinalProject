

# File Name : location_Decryptor.py
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
#   Handles the location decryption task. Contains a function (`get_location_indices`)
#   to read the EncryptedGroupHints JSON file and extract the list of indices 
#   for a specific team. Also contains the main decryption function 
#   (`decrypt_location_from_indices`) which uses these indices and the 
#   `english_Loader` module to reconstruct the location string.
# Citations: {List any websites, books, or specific resources used}
#   - Google Gemini (generative AI assistant): Assistance with code structure, 
#     debugging, function implementation, docstrings, and explaining concepts. 
#     URL: https://gemini.google.com/ 

# Anything else that's relevant: {Add any notes if applicable}
import json
import os 
from .english_Loader import load_word_list 

def get_location_indices(hints_filepath, team_name):
    """
    Reads the JSON dictionary file and returns the list of indices for the specified team.

    @param hints_filepath (str): Path to the JSON file containing team hints.
    @param team_name (str): The name of the team to look up.
    @return (list[str] or None): The list of index strings for the team, or None if not found/error.
    """
    if not os.path.exists(hints_filepath):
        print(f"Error: Location hints file not found at '{hints_filepath}'")
        return None
        
    try:
        with open(hints_filepath, 'r', encoding='utf-8') as f:
            all_hints = json.load(f) 

        indices = all_hints.get(team_name)

        if indices is not None:
            print(f"Found indices for team '{team_name}'")
            return indices 
        else:
            print(f"Warning: Team '{team_name}' not found as a key in {os.path.basename(hints_filepath)}")
            return None 

    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {os.path.basename(hints_filepath)}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred reading location hints file: {e}")
        return None


def decrypt_location_from_indices(indices, dictionary_filepath):
    """
    Uses indices to look up words in the dictionary file (loaded via helper).

    @param indices (list[str]): The list of index strings to look up.
    @param dictionary_filepath (str): Path to the UCEnglish.txt dictionary file.
    @return (str): The decrypted location string (words joined by spaces), or an error message.
    """
    if not indices:
        return "Error: No indices provided for location decryption."

    word_list = load_word_list(dictionary_filepath)
    
    if word_list is None:
        return "Error: Failed to load word list for location decryption."
        
    decrypted_words = []
    word_list_length = len(word_list)
    
    for index_str in indices:
        try:
            index = int(index_str) - 1 
            if 0 <= index < word_list_length:
                word = word_list[index] 
                decrypted_words.append(word)
            else:
                 print(f"Warning: Location index {index + 1} is out of bounds (list size: {word_list_length}).")
                 decrypted_words.append(f"[BAD_IDX:{index + 1}]")
        except ValueError:
             print(f"Warning: Could not convert location index '{index_str}' to integer.")
             decrypted_words.append(f"[NAN:{index_str}]")
        except Exception as e:
            print(f"Error processing location index '{index_str}': {e}")
            decrypted_words.append(f"[PROC_ERR]")

    return ' '.join(decrypted_words)
# ================================================================
# End of File: decryption/location.py
# ================================================================
















