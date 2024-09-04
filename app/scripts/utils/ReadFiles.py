import os
from typing import Optional


def get_filenames_from_dir(directory_path: str, app_path: Optional[str] = None) -> list:
    root_dir = ""
    if isinstance(app_path, str):
        root_dir = app_path
    else:
        root_dir = os.environ.get('APP_PATH', '/app/Resume-Matcher')

    directory_path = f"{root_dir}/{directory_path}"
    filenames = [
        f
        for f in os.listdir(directory_path)
        if os.path.isfile(os.path.join(directory_path, f)) and f != ".DS_Store" and f != ".gitkeep"
    ]
    return filenames
