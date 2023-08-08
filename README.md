# File Cleaner

The File Cleaner is a Python script that allows you to sort files in a folder based on their file types and move them to corresponding folders.

## Usage

1. Run the script by executing the `main()` function.
2. Enter the path to the folder you want to clean when prompted.
3. The script will prompt you to enter the file types and their corresponding extensions. The file types and extensions should be entered in the following format:
   ```
   file_type: [extension1, extension2, ...]
   ```
   For example:
   ```
   video: [.avi, .mp4]
   photo: [.jpg, .jpeg, .png, .svg]
   music: [.mp3, .wav]
   documents: [.docx, .doc, .txt, .pdf]
   presentation: [.pptx]
   ```
4. The script will then sort the files in the specified folder based on their file types and move them to corresponding folders.
5. After the sorting is complete, the script will display the number of files moved to each folder.

## Example

Here is an example of how to use the File Cleaner:

```
Введите путь к папке: /path/to/folder
video: [.avi, .mp4]
photo: [.jpg, .jpeg, .png, .svg]
music: [.mp3, .wav]
documents: [.docx, .doc, .txt, .pdf]
presentation: [.pptx]
```

```
Создана папка video и перемещено 2 файлов
Создана папка photo и перемещено 5 файлов
Создана папка music и перемещено 3 файлов
Создана папка documents и перемещено 4 файлов
Создана папка presentation и перемещено 1 файлов
```

In this example, the script prompts for the folder path and file types. It then creates folders for each file type and moves the corresponding files to their respective folders. Finally, it displays the number of files moved to each folder.

## Dependencies

The File Cleaner script requires the following dependencies:

- Python 3.x
- `os` module
- `shutil` module

Make sure you have Python installed on your system and the required modules are available before running the script.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
