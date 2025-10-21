import sys
from pathlib import Path
from colorama import Fore

SYMBOL_SPACE = " "
SYMBOL_PREFIX_DIR = "📂"
SYMBOL_PREFIX_FILE = "📜"


def visualize_directory(target_path: Path) -> None:
    root_name = target_path.name if target_path.name else str(target_path)
    print(f" {Fore.BLUE}📦 {root_name}")
    display_content(target_path, prefix="")


def display_content(current_path: Path, prefix: str) -> None:
    try:
        contents = sorted(
            list(current_path.iterdir()), key=lambda p: (p.is_file(), p.name)
        )
    except PermissionError:
        print(
            f"{Fore.LIGHTBLACK_EX}{prefix} L {Fore.RED}Permission denied: {current_path.name}"
        )
        return
    except Exception as e:
        print(
            f"{Fore.LIGHTBLACK_EX}{prefix} L {Fore.RED}Reading error: {current_path.name} ({e})"
        )
        return

    count_content = len(contents)
    for index, item in enumerate(contents):
        is_last = index == count_content - 1
        connector = " L " if is_last else " |-"
        line = f"{Fore.LIGHTBLACK_EX}{prefix}{connector}{SYMBOL_SPACE}"

        if item.is_dir():
            print(f"{line}{Fore.BLUE}{SYMBOL_PREFIX_DIR} {item.name}")
            new_prefix = (
                f"{prefix} |{SYMBOL_SPACE}"
                if not is_last
                else f"{prefix}{SYMBOL_SPACE}"
            )
            display_content(item, new_prefix)

        elif item.is_file():
            print(f"{line}{Fore.GREEN}{SYMBOL_PREFIX_FILE} {item.name}")


def main() -> None:
    if len(sys.argv) < 2:
        print(
            f"{Fore.RED}Error: You must specify the path to the directory as a command line argument."
        )
        print(f"Usage: python {Path(sys.argv[0]).name} /path/to/directory")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"{Fore.RED}Error: Path '{input_path}' not found.")
        sys.exit(1)

    if not input_path.is_dir():
        print(f"{Fore.RED}Error: Path '{input_path}' is not directory.")
        sys.exit(1)

    visualize_directory(input_path)


if __name__ == "__main__":
    main()
