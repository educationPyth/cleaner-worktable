import os
import shutil
from sqlite_db import DatabaseUserSettings


class UserInput:
    def __init__(self, name_database: str):
        self.name_database = name_database
        self.path = ''

    def set_path(self, folder_path):
        self.path = folder_path

    def get_path(self):
        return self.path

    def set_sittings(self, name_folder: str, appropriate: str):
        db = DatabaseUserSettings(self.name_database)
        with db.conn:
            db.set_data(name_folder, appropriate)

    def clear_settings(self):
        db = DatabaseUserSettings(self.name_database)
        with db.conn:
            db.clear_table()


class CleanerWorktable:
    def __init__(self, folder_path: str):
        self.full_folder_path = folder_path

def sort_folder(folder_path):
    # get list file of folder
    files = os.listdir(folder_path)

    # create dict to story file types  and their corresponding extensions
    file_types = {
        "video": [".avi", ".mp4"],
        "photo": [".jpg", ".jpeg", ".png", ".bmp"],
        "document": [".doc", ".docx", ".pdf", ".txt"],
        "music": [".mp3", ".wav"],
        "other": []
    }

    sorted_files = {

    }

    # looping through files and determining their types
    for file in files:
        if os.path.isfile(os.path.join(folder_path, file)):
            file_extension = os.path.splitext(file)[1].lower()

            for key, values in file_types.items():
                if file_extension in values:
                    sorted_files.setdefault(key, []).append(file)
                    break
            else:
                sorted_files.setdefault("other", []).append(file)

    # create folders to files for corresponding extensions
    for key in sorted_files:
        folder_name = key
        folder_new_path = os.path.join(folder_path, folder_name)
        os.makedirs(folder_new_path, exist_ok=True)
    # move file to appropriate folder
        for file in sorted_files[key]:
            file_path = os.path.join(folder_path, file)
            file_new_path = os.path.join(folder_new_path, file)
            shutil.move(file_path, file_new_path)

        print(f"Создана папка {folder_name} и перемещено {len(sorted_files[key])} файлов")


if __name__ == "__main__":
    sort_folder('')
