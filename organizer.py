import os
import shutil

# Folder to organize (change this)
folder_path = "test_folder"

# File type mapping
file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Code": [".py", ".cpp", ".js"]
}

# Create folders
for category in file_types:
    os.makedirs(os.path.join(folder_path, category), exist_ok=True)

# Move files
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        for category, extensions in file_types.items():
            if any(file.endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(folder_path, category, file))
                break

print("Files organized successfully!")
