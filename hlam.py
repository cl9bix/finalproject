import argparse
from pathlib import Path
from shutil import copyfile
from concurrent.futures import ThreadPoolExecutor
import logging

parser = argparse.ArgumentParser(description='Hlam sorter')
parser.add_argument('--source', '-s', help="Source folder", required=True)
parser.add_argument('--output', '-o', help="Output folder", default='dist')

args = vars(parser.parse_args())

source = Path(args.get('source'))
output = Path(args.get('output'))

folders = []


def grab_folders(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            grab_folders(el)


def copy_file(path: Path) -> None:
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix[1:]
            new_folder = output / ext
            try:
                new_folder.mkdir(parents=True, exist_ok=True)
                copyfile(el, new_folder / el.name)
            except OSError as err:
                logging.error(err)


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR, format="%(threadName)s %(message)s")

    grab_folders(source)

    with ThreadPoolExecutor() as executor:
        executor.map(copy_file, folders)

    print("Можна видалити стару папку")
