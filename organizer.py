"""
Automatic File Organizer
------------------------
Sorts the files inside a folder into sub-folders based on their type
(Images, Documents, Videos, etc.).

How to run:
    python organizer.py
"""

import shutil
from pathlib import Path

# Which file extensions go into which folder.
# You can add or change extensions here to customise the organizer.
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx",
                  ".xls", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".m4a"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".json"],
    "Programs": [".exe", ".msi", ".apk"],
}

OTHER_FOLDER = "Others"  # for files that don't match any category


def get_category(extension):
    """Return the folder name for a file extension (e.g. '.pdf' -> 'Documents')."""
    extension = extension.lower()
    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category
    return OTHER_FOLDER


def get_unique_path(destination):
    """If a file with the same name already exists, add (1), (2)... to the name."""
    if not destination.exists():
        return destination

    counter = 1
    while True:
        new_name = f"{destination.stem} ({counter}){destination.suffix}"
        new_path = destination.with_name(new_name)
        if not new_path.exists():
            return new_path
        counter += 1


def plan_moves(folder):
    """Look at the files in the folder and decide where each one should go."""
    moves = []
    this_script = Path(__file__).resolve()

    for item in folder.iterdir():
        # Only organize files (skip folders), hidden files and this script itself
        if not item.is_file():
            continue
        if item.name.startswith("."):
            continue
        if item.resolve() == this_script:
            continue

        category = get_category(item.suffix)
        moves.append((item, folder / category / item.name))

    return moves


def organize(folder):
    """Move the files into their category folders."""
    moves = plan_moves(folder)

    if not moves:
        print("No files to organize in this folder.")
        return

    # Show a preview first so nothing surprising happens
    print(f"\nFound {len(moves)} file(s). Here is the plan:\n")
    for source, destination in moves:
        print(f"  {source.name}  ->  {destination.parent.name}/")

    answer = input("\nProceed and move these files? (y/n): ").strip().lower()
    if answer != "y":
        print("Cancelled. No files were moved.")
        return

    moved_count = 0
    summary = {}

    for source, destination in moves:
        destination.parent.mkdir(exist_ok=True)       # create folder if needed
        final_path = get_unique_path(destination)     # avoid overwriting files
        try:
            shutil.move(str(source), str(final_path))
            moved_count += 1
            summary[destination.parent.name] = summary.get(destination.parent.name, 0) + 1
        except (PermissionError, OSError) as error:
            print(f"  Could not move {source.name}: {error}")

    print(f"\nDone! Moved {moved_count} file(s):")
    for category, count in sorted(summary.items()):
        print(f"  {category}: {count}")


def main():
    print("=== Automatic File Organizer ===")
    path_text = input("Enter the full path of the folder to organize: ").strip().strip('"').strip("'")

    folder = Path(path_text).expanduser()

    if not folder.exists() or not folder.is_dir():
        print("That folder does not exist. Please check the path and try again.")
        return

    organize(folder)


if __name__ == "__main__":
    main()
