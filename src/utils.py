from constants import FileMode
import logging
import json

LOGGER = logging.getLogger(__name__)

class FileService:
    @staticmethod
    def _open_file(file_path, mode):
        """Attempt to open a file and return the file object or None on failure."""
        try:
            return open(file_path, mode)
        except IOError as ex:
            LOGGER.error(f"Failed to open file {file_path}: {ex}")
            return None

class JsonFileService:
    @staticmethod
    def read(file_path):
        file = FileService._open_file(file_path, FileMode.READ)
        if file:
            try:
                return json.load(file)
            except json.JSONDecodeError as ex:
                LOGGER.error(f"Failed to decode JSON from {file_path}: {ex}")
            finally:
                file.close()

class TextFileService:
    @staticmethod
    def read_all(file_path):
        file = FileService._open_file(file_path, FileMode.READ)
        if file:
            try:
                return file.read()
            finally:
                file.close()

    @staticmethod
    def read_lines(file_path):
        file = FileService._open_file(file_path, FileMode.READ)
        if file:
            try:
                return file.readlines()
            finally:
                file.close()