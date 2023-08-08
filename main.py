import os
import shutil


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


def main():

    user_input_path = input('Введите путь к папке: ')
    user_input_file_types = {
        "video": [".avi", ".mp4"],
        "photo": [".jpg", ".jpeg", "png", ".svg"],
        "music": [".mp3", ".wav"],
        "documents": [".docx", ".doc", ".txt", ".pdg"],
        "presentation": [".pptx"]
    }

    cleaner = CleanerWorktable(user_input_path, user_input_file_types)
    cleaner.sort_folder()
    return


if __name__ == "__main__":
    main()
