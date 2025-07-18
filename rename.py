import os
folder_path = "raw_data(images)"

image_files = sorted(os.listdir(folder_path))

for i, filename in enumerate(image_files, start=1):

    old_path = os.path.join(folder_path, filename)
    new_filename = f"{i}.jpg"
    new_path = os.path.join(folder_path, new_filename)

    os.rename(old_path, new_path)

print("Renaming complete.")
