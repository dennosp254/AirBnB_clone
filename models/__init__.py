#!/usr/bin/python3
"""
Intializes the module global (singleton) variables
"""

from .engine.file_storage import FileStorage
"""
Retries the storage instance
"""
storage = FileStorage()
storage.reload()
