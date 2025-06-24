from fastapi import APIRouter
import os
import shutil
import logging

router = APIRouter()

@router.post("/cleanup-temp")
def cleanup_temp_folders():
    folders = ["temp_inputs", "temp_outputs"]
    deleted_files = []

    for folder in folders:
        if os.path.exists(folder):
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    os.remove(file_path)
                    deleted_files.append(file_path)
                except Exception as e:
                    logging.error(f"Failed to delete {file_path}: {e}")

    return {
        "status": "✅ Temp folder cleanup complete",
        "deleted_files": deleted_files
    }
