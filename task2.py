from utils import get_file_content


def get_cats_info(path: str) -> list[dict[str, str]] | None:
    try:
        content = get_file_content(path)
    except Exception as e:
        print(e)
        return None

    cats = []
    keys = ["id", "name", "age"]
    for line in content:
        cat_info = line.strip().split(",")
        if len(cat_info) != 3:
            print(f"'{line}' format is incorrect.")
            continue
        cats.append(dict(zip(keys, cat_info)))

    return cats
