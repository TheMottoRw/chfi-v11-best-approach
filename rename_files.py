import os


def rename_files_incrementally(directory):
    # Get a list of files in the specified directory
    files = os.listdir(directory)

    # Filter out directories (we only want files)
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]

    # Sort files if needed
#     print(files[:5])
    files.sort()
#     print(files[:5])
#     quit()
    # Rename each file
    for index, file in enumerate(files, start=1):
        # Get the file extension
        file_extension = os.path.splitext(file)[1]
        if not file.startswith("Screenshot"):
            continue

        # Create new filename with incremented number
        new_name = f"{(index)}{file_extension}"

        # Get the full path of the old and new file
        old_file = os.path.join(directory, file)
        new_file = os.path.join(directory, new_name)

        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed: {file} -> {new_name}")


# Example usage:
directory = "/home/legion/Pictures/Screenshots/chfi/"
rename_files_incrementally(directory)
