import re
from pathlib import Path


def get_file_content(path) -> list[str]:
    path = Path(path)
    if not (path.exists() and path.is_file()):
        raise Exception(f"File {path} does not exist in current directory.")
    try:
        with open(path, "r") as file:
            return file.readlines()
    except Exception as e:
        raise e


def normalize_phone(phone_number: str) -> str:
    clean_number = re.sub(r"[^\d]", "", phone_number)

    if clean_number.startswith("0"):
        clean_number = f"+38{clean_number}"
    elif clean_number.startswith("8"):
        clean_number = f"+3{clean_number}"
    elif clean_number.startswith("3"):
        clean_number = f"+{clean_number}"

    return clean_number
