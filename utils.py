import re
from pathlib import Path

from colorama import Fore


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


def validate_phone(phone_number: str) -> bool:
    pattern = re.compile(r"^\+380\d{9}$")
    return bool(pattern.match(phone_number))


def upsert_contact(
    name: str, phone_number: str, reference_book: dict[str, str], command: str
) -> str:
    normalized_phone_number = normalize_phone(phone_number)
    if validate_phone(normalized_phone_number):
        reference_book[name] = normalized_phone_number
        return "Contact added!" if command == "add" else "Contact changed!"
    else:
        return f"{Fore.RED}You have entered an invalid number. A Ukrainian mobile phone number starting with +380 and containing 9 additional digits (e.g. +380981234567) is expected."
