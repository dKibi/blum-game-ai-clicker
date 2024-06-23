# Standard Libraries
from typing import Optional
import os
import shutil

# Third-party Libraries
from loguru import logger
import yaml


def create_directory_if_not_exist(directory_path: str) -> None:
    """
    Create a directory if it doesn't exist.

    :param directory_path: The path to the directory.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        logger.debug(f"Directory '{directory_path}' has been created.")
    else:
        logger.debug(f"Directory '{directory_path}' already exists. No changes made.")


def create_file_from_template_if_not_exist(destination_file_path: str, file_template_path: str) -> None:
    if not os.path.exists(destination_file_path):
        copy_file(source_path=file_template_path, destination_path=destination_file_path)


def copy_file(source_path: str, destination_path: str) -> None:
    """
    Copy a file from the source path to the destination path.

    :param source_path: The path to the source file.
    :param destination_path: The path to the destination file.
    """
    try:
        shutil.copy2(source_path, destination_path)
    except FileNotFoundError:
        logger.error(f"Could not make a copy to {destination_path}, there is no source file at {source_path}.")
        raise


def load_yaml(file_path: str) -> Optional[dict]:
    """
    Load YAML file.

    :param file_path: The path to the YAML file.
    :return: The contents of the YAML file or None if file was not found/an error occurred.
    """
    try:
        with open(file_path, 'r') as file:
            content = yaml.safe_load(file)
            return content
    except FileNotFoundError:
        logger.error(f"File {file_path} does not exist.")
        return None
    except Exception as e:
        logger.error(f"Could not parse YAML content from {file_path} due to unexpected error: {e}.")
        return None
