#!/usr/bin/python3
from zipfile import ZipFile, ZIP_DEFLATED
import os
from datetime import datetime

ARCHIVE_PATH = os.path.join(
    os.environ["HOME"], datetime.now().strftime("%Y%m%d_%H%M") + ".zip"
)
FOLDER_PATH = os.path.join(os.environ["HOME"], "Documents")

with ZipFile(ARCHIVE_PATH, "w", ZIP_DEFLATED) as zip_object:
    for folder_name, _, file_names in os.walk(FOLDER_PATH):
        if any(name in folder_name.split("/") for name in ["env", "venv", ".env", ".venv"]):
            continue

        for file_name in file_names:
            file_path = os.path.join(folder_name, file_name)
            zip_object.write(file_path, os.path.relpath(file_path, FOLDER_PATH))
            print(f"Added file {file_path} to archive")

if os.path.exists(ARCHIVE_PATH):
    print("ZIP file created")
else:
    print("ZIP file not created")

