import os
import shutil

def organize_files(directory):
    # Firstly, check if the given directory exists
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Change to the target directory
    os.chdir(directory)

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Skip directories
        if os.path.isfile(filename):
            # Get the file extension
            file_ext = filename.split('.')[-1] if '.' in filename else 'no_extension'

            # Create a directory for the file extension if it does not exist
            if not os.path.exists(file_ext):
                os.makedirs(file_ext)

            # Move the file to the appropriate directory
            shutil.move(filename, os.path.join(file_ext, filename))

    print("Files have been organized.")

# Example usage
if __name__ == "__main__":
  #Change name here.
   organize_files('directory_path')
