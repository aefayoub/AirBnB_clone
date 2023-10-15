#!/usr/bin/python3

"""import all modules and packages needed"""


from models.engine.file_storage import FileStorage

# Create an instance of the FileStorage class
storage = FileStorage()

# Reload any stored data from a previous session
storage.reload()
