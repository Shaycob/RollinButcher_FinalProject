

# File Name : english_Loader.py
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
#   Provides a reusable function (`load_word_list`) to load the contents 
#   of the UCEnglish.txt dictionary file into a Python list. Includes basic 
#   caching to avoid redundant file reads if called multiple times. Handles 
#   file opening errors.
# Citations: {List any websites, books, or specific resources used}
#   - Google Gemini (generative AI assistant): Assistance with code structure, 
#     debugging, function implementation, docstrings, and explaining concepts. 
#     URL: https://gemini.google.com/ 

# Anything else that's relevant: {Add any notes if applicable}
import os

_word_list_cache = None 

def load_word_list(dictionary_filepath):
    """
    Loads words from the dictionary file into a list.
    Uses a simple cache to avoid reloading if called multiple times.

    @param dictionary_filepath (str): Path to the UCEnglish.txt file.
    @return (list[str] or None): A list of words, or None if loading fails.
    """
    global _word_list_cache
    if _word_list_cache is not None:
        return _word_list_cache

    if not os.path.exists(dictionary_filepath):
        print(f"Error: Dictionary file not found at '{dictionary_filepath}'")
        return None
        
    try:
        with open(dictionary_filepath, 'r', encoding='utf-8') as f:
            loaded_words = [line.strip() for line in f.readlines()]
        
        print(f"Successfully loaded {len(loaded_words)} words from {os.path.basename(dictionary_filepath)}")
        _word_list_cache = loaded_words
        return loaded_words

    except Exception as e:
        print(f"Error reading dictionary file '{dictionary_filepath}': {e}")
        _word_list_cache = None 
        return None

# ================================================================
# End of File: decryption/english_Loader.py
# ================================================================


