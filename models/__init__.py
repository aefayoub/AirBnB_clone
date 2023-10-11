#!/usr/bin/python3
"""import all modules and packages needed"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
