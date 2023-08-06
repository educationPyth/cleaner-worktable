import os
import shutil
from datetime import datetime
from sqlite_db import DatabaseUserSettings


input_user_path_folder = r'D:\test folder sort'
input_user_name_database = 'какое-то название'
current_date = datetime.now()
formatted_date = current_date.strftime("%d_%m_%Y")
formatted_new_database = formatted_date
name_table = f"Settings_{formatted_new_database}"

input_user_name_folder = "video"
input_user_appropriate = [".avi", "mp4"]


class UserInput:
    def __init__(self, name_database: str):
        self.name_database = name_database
        self.db = DatabaseUserSettings(self.name_database)
        self.path = ''

    def set_path(self, folder_path):
        self.path = folder_path

    def get_path(self):
        return self.path

    def set_sittings(self, name_folder: str, appropriate: list):
        with self.db.conn:
            self.db.set_data(name_folder, appropriate)

    def get_settings(self):
        with self.db.conn:
            print(f"Блок кода в классе UserInput get_settings {self.db.get_data()}")
            return self.db.get_data()

    def clear_settings(self):
        with self.db.conn:
            self.db.clear_table()


class CleanerWorktable:
    def __init__(self, folder_path: str, file_types: dict):
        # get path to folder
        self.full_folder_path = folder_path
        # get list file of folder
        self.files = os.listdir(self.full_folder_path)

        self.file_types = file_types
        # create dict to story file types  and their corresponding extensions
        self.sorted_files = {}

    def sort_folder(self):
        # looping through files and determining their types
        for file in self.files:
            if os.path.isfile(os.path.join(self.full_folder_path, file)):
                file_extension = os.path.splitext(file)[1].lower()

                for key, values in self.file_types.items():
                    if file_extension in values:
                        self.sorted_files.setdefault(key, []).append(file)
                        break
                else:
                    self.sorted_files.setdefault("other", []).append(file)

        # create folders to files for corresponding extensions
        for key in self.sorted_files:
            folder_name = key
            folder_new_path = os.path.join(self.full_folder_path, folder_name)
            os.makedirs(folder_new_path, exist_ok=True)
        # move file to appropriate folder
            for file in self.sorted_files[key]:
                file_path = os.path.join(self.full_folder_path, file)
                file_new_path = os.path.join(folder_new_path, file)
                shutil.move(file_path, file_new_path)

            print(f"Создана папка {folder_name} и перемещено {len(self.sorted_files[key])} файлов")


def get_data_user():
    user = UserInput(name_table)
    user.set_path(input_user_path_folder)
    user.set_sittings(input_user_name_folder, input_user_appropriate)

    print(user.get_settings())
    return user.get_settings()


def main():
    get_data_user()


if __name__ == "__main__":
    main()
