import os

def batch_rename(folder, base_name, extension):
    files = [f for f in os.listdir(folder) if f.lower().endswith(extension.lower())]
    files.sort() # this will not do much

    if not files:
        print("No file founded")
        return
    
    for idx, file in enumerate(files, start=1):
        new_name= f"{base_name}_{idx}_{extension}"
        print(f"{file} -> {new_name}")

    confirmation = input("press (y) to confirm or (n) to reject: ").strip().lower()

    if confirmation != 'y':
        print('Cancelling your renaming')
        return
    
    for idx, file in enumerate(files, start=1):
        src = os.path.join(folder, file)
        new_name= f"{base_name}_{idx}_{extension}"
        dest  = os.path.join(folder, new_name)
        os.rename(src, dest)
    print(f"Renamed {len(files)} files successfully")


if __name__ == "__main__":
    folder = input("Enter folder path or leave blank if in current directory: ").strip()
    folder = folder or os.getcwd()

    if not os.path.isdir(folder):
        print("Invalid folder")
    else:
        base_name = input("Enter base name for files: ").strip()
        extension = input("Enter extension name for files: ").strip()

        batch_rename(folder, base_name, extension)