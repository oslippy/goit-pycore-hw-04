from colorama import Fore

from utils import normalize_phone


def add_contact(name: str, phone_number: str, reference_book: dict[str, str]) -> str:
    if name not in reference_book:
        reference_book[name] = normalize_phone(phone_number)
        return "Contact added!"
    else:
        return f"{Fore.RED}'{name}' already exists in reference book."


def change_contact(name: str, phone_number: str, reference_book: dict[str, str]) -> str:
    if name in reference_book:
        reference_book[name] = normalize_phone(phone_number)
        return "Contact changed!"
    else:
        return f"{Fore.RED}Contact '{name}' doesn't exist."


def show_phone(name: str, reference_book: dict[str, str]) -> str:
    if contact := reference_book.get(name):
        return f"{Fore.LIGHTYELLOW_EX}{contact}"
    else:
        return f"{Fore.RED}Contact not found."


def show_all(reference_book: dict[str, str]) -> str:
    output = f"{Fore.YELLOW}CONTACTS:\n"
    if len(reference_book) == 0:
        output += f"{Fore.YELLOW}is empty..."
        return output

    for name, phone_number in reference_book.items():
        output += f"{Fore.LIGHTYELLOW_EX}{name}: {Fore.LIGHTYELLOW_EX}{phone_number}\n"
    return output if not output.endswith("\n") else output[:-2]


COMMANDS = {
    "add": add_contact,
    "change": change_contact,
    "phone": show_phone,
    "all": show_all,
}


def parse_input(user_input: str):
    command, *args = user_input.strip().split()
    command = command.lower()
    return command, args


def main():
    print(f"{Fore.GREEN}Welcome to the assistant bot!")
    reference_book = {}
    while True:
        input_command = input(f"{Fore.BLUE}Enter a command: ")
        command, args = parse_input(input_command)
        if command in ("exit", "close"):
            print(f"{Fore.GREEN}Good bye!")
            break
        elif command == "hello":
            print(f"{Fore.GREEN}Hello! How can I help you?")
        elif command not in COMMANDS:
            print(f"{Fore.RED}Invalid command.")
        else:
            try:
                handler = COMMANDS.get(command)
                print(handler(*args, reference_book=reference_book))
            except TypeError as e:
                print(f"{Fore.RED}{e}")


if __name__ == "__main__":
    main()
