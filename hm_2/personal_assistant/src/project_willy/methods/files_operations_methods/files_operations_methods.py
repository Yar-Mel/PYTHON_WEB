
from methods.imports import os, Path, pickle, json, csv


class FileOperations:

    AUTOSAVE_PATH = Path(os.getcwd()) / 'willy_autosave.bin'

# TXT
    def export_to_txt(file_path, data: str) -> None:
        with open(file_path, 'w') as fh:
            fh.write(data)

# PICKLE
    def export_to_pickle(file_path, data) -> None:
        with open(file_path, "wb") as fh:
            pickle.dump(data, fh)

    def autosave_to_pickle(file_path, *args) -> None:
        with open(file_path, "wb") as fh:
            pickle.dump(args, fh)

    def import_from_pickle(file_path):
        with open(file_path, "rb") as fh:
            return pickle.load(fh)

# JSON
    def export_to_json(file_path, data) -> None:
        with open(file_path, "w") as fh:
            json.dump(data, fh, indent=1)

# CSV
    def export_to_csv(file_path, data: list) -> None:
        with open(file_path, 'w', newline='') as fh:
            record_writer = csv.writer(fh)
            for row in data:
                record_writer.writerow(row)
