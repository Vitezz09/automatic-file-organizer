# Automatic File Organizer

A simple Python mini project that automatically sorts the files in a messy folder (like Downloads) into neat sub-folders such as Images, Documents, Videos, Audio, Archives and more.

## Features

- Sorts files by extension into category folders
- Shows a preview of what will be moved and asks for confirmation first
- Never overwrites files: duplicate names become `file (1).txt`, `file (2).txt`, etc.
- Skips hidden files, existing folders and the script itself
- Easy to customise: edit the `FILE_TYPES` dictionary to add your own categories

## Requirements

- Python 3.6 or newer
- No extra libraries needed (uses only the standard library: `pathlib` and `shutil`)

## How to run

1. Download or clone this repository
2. Open a terminal / command prompt in the project folder
3. Run:

   ```
   python organizer.py
   ```

4. Enter the full path of the folder you want to organize, for example:
   - Windows: `C:\Users\YourName\Downloads`
   - Mac/Linux: `/home/yourname/Downloads`
5. Check the preview and type `y` to confirm

## Example

Before:

```
Downloads/
  photo.jpg
  notes.pdf
  song.mp3
  setup.zip
```

After:

```
Downloads/
  Images/     photo.jpg
  Documents/  notes.pdf
  Audio/      song.mp3
  Archives/   setup.zip
```

## How it works

1. Reads every file in the chosen folder
2. Looks at the file extension (`.jpg`, `.pdf`, ...) and finds its category
3. Creates the category folder if it doesn't exist
4. Moves the file there using `shutil.move`

## Concepts used

`pathlib`, `shutil`, dictionaries, functions, loops, user input, exception handling

## Author

Vitez Mohanty - Chandigarh University - 26MCD-1(A)/26MCD10018
