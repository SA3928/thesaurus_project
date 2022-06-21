# thesaurus_project
This is a thesaurus with a CLI written in Python 3.8 with a JSON file database.
The program fetches words from a JSON file. Incase of spelling errors, it asks the user if they meant something else.
This is achieved by using the "difflib" library in Python.
This program runs in a loop, after each search asking the user if they wish to search again. On getting "N" or "n" (for "No") as an input, it terminates and exits the program.
