import os
import shutil
from PyQt5.QtWidgets import QApplication, QMainWindow
from form import Ui_MainWindow


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.text = self.ui.textEdit
        self.ui.btn_run.clicked.connect(self.send_data)

    def send_data(self):
        # Получаем текст из поля lineEdit
        user_path_folder = self.ui.input_path.text()
        file_types_default = {
            "video": [".avi", ".mp4", ".mov", ".wmv", ".mkv"],
            "audio": [".mp3", ".wav", ".flac", ".aac", ".wma"],
            "picture": [".jpg", ".jpeg", "png", ".svg", ".gif", ".bmp", ".tiff", ".raw", ".ico", ".webp"],
            "documents": [".docx", ".doc", ".txt", ".pdf", ".xlsx"],
            "presentation": [".pptx", ".key", ".odp", ".ppt"]
        }
        # Создаем экземпляр класса CleanerWorktable
        cleaner = CleanerWorktable(user_path_folder, file_types_default)
        # FIXME
        text = ','.join(cleaner.sort_folder())
        print(text)

        cleaner.sort_folder()


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
        data_success = []
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

            data_success.append(f"Создана папка {folder_name} и перемещено {len(self.sorted_files[key])} файлов")
        return data_success


def main():
    cleaner_app = MyApp()
    cleaner_app.show()
    return app.exec_()


if __name__ == "__main__":
    app = QApplication([])
    main()
