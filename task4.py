from colorama import Fore

from utils import normalize_phone


REFERENCE_BOOK = {}


def add_contact(name: str, phone_number: str) -> None:
    if name not in REFERENCE_BOOK:
        REFERENCE_BOOK[name] = normalize_phone(phone_number)
        print("Contact added!")
    else:
        print(f"{Fore.RED}'{name}' already exists in reference book.")


def change_contact(name: str, phone_number: str) -> None:
    if name in REFERENCE_BOOK:
        REFERENCE_BOOK[name] = normalize_phone(phone_number)
        print("Contact changed!")
    else:
        print(f"{Fore.RED}Contact '{name}' doesn't exist.")


def show_phone(name: str) -> None:
    if contact := REFERENCE_BOOK.get(name):
        print(f"{Fore.YELLOW}{contact}")
    else:
        print(f"{Fore.RED}Contact not found.")


def show_all() -> None:
    print(f"{Fore.YELLOW}CONTACTS:")
    if len(REFERENCE_BOOK) == 0:
        print(f"{Fore.BLUE}is empty...")
        return
    for name, phone_number in REFERENCE_BOOK.items():
        print(f"{Fore.LIGHTYELLOW_EX}{name}: {Fore.LIGHTYELLOW_EX}{phone_number}")


COMMANDS = {
    "add": add_contact,
    "change": change_contact,
    "phone": show_phone,
    "all": show_all,
}


def parse_input(command: str):
    command, *args = command.strip().split()
    command = command.lower()
    if command in ("exit", "close"):
        print(f"{Fore.GREEN}Good bye!")
        exit(0)
    elif command == "hello":
        print(f"{Fore.GREEN}Hello! How can I help you?")
    elif command not in COMMANDS:
        print(f"{Fore.RED}Invalid command.")
    else:
        try:
            handler = COMMANDS.get(command)
            handler(*args)
        except TypeError as e:
            print(f"{Fore.RED}{e}")


def main():
    print(f"{Fore.GREEN}Welcome to the assistant bot!")
    while True:
        input_command = input(f"{Fore.BLUE}Enter a command: ")
        parse_input(input_command)


if __name__ == "__main__":
    main()
