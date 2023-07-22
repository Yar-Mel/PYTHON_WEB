import re
import os
from pathlib import Path
from threading import Thread

# ---------------------------------------- SETTINGS ----------------------------------------


SETTINGS = {
    'documents': ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
    'video': ['.avi', '.mp4', '.mov', '.mkv'],
    'audio': ['.mp3', '.ogg', '.wav', '.amr'],
    'images': ['.jpeg', '.png', '.jpg', '.svg'],
    'archives': ['.zip', '.tar']
}

# ---------------------------------------- NORMALIZE ----------------------------------------
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = (
    "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s",
    "t", "u", "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g"
)

MAP = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    MAP.update({ord(c): l, ord(c.upper()): l.upper()})


def normalize(file: Path) -> str:
    file_name = file.name.replace(file.suffix, '')
    edited_file_name = file_name.translate(MAP)
    edited_file_name = re.sub(r'\W', '_', edited_file_name)
    return f'{edited_file_name}{file.suffix}'

# ---------------------------------------- PARSER ----------------------------------------


files = []
folders = []


def scan_folder(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_dir():
            folders.append(item)

            # with threads
            threads = []
            th = Thread(target=scan_folder, args=(item,))
            th.start()
            threads.append(th)
            [th.join() for th in threads]

            # without threads
            # scan_folder(item)
        else:
            files.append(item)


# ---------------------------------------- HANDLERS ----------------------------------------


def file_handle(target_folder: Path, file_path: Path, ) -> None:
    for folder, extensions in SETTINGS.items():
        if file_path.suffix.lower() in extensions:
            moving_file(file_path, target_folder / folder)


def moving_file(file_path: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    file_path.replace(target_folder / normalize(file_path))


def handle_folder(folder: Path) -> None:
    """Removing empty folders"""

    if not os.listdir(folder):
        try:
            folder.rmdir()
        except OSError:
            print(f'{folder} removing error')
    else:
        os.rename(folder, Path(str(folder).translate(MAP)))


def main() -> None:
    while True:
        user_input = input("\nPut the path to the folder, please.\n>>> ")
        target_folder = Path(user_input)

        if target_folder.is_dir():
            # scan folders
            scan_folder(target_folder)

            # handle files
            for file in files:

                # with threads
                threads = []
                th = Thread(target=file_handle, args=(target_folder, file))
                th.start()
                threads.append(th)
                [th.join() for th in threads]

                # without threads
                # file_handle(target_folder, file)

            # handle folders
            for folder in folders:

                # with threads
                threads = []
                th = Thread(target=handle_folder, args=(folder,))
                th.start()
                threads.append(th)
                [th.join() for th in threads]

                # without threads
                # handle_folder(folder)

            print("\nDone!\n")

            break
        elif user_input == "exit":
            print("Cancelling...")
            break
        else:
            print("Wrong directory!")


if __name__ == '__main__':
    main()

# /home/yaroslav/Public/hm_3/garbage
