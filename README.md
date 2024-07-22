# File Organizer Script

## Overview

This Python script organizes files in a specified directory by moving them into subdirectories based on their file extensions. For example, all `.jpg` files will be moved into a `jpg` folder, `.txt` files into a `txt` folder, and so on. Files without an extension will be placed in a directory named `no_extension`.

## Features

- Creates subdirectories for each file extension.
- Moves files into their corresponding subdirectories.
- Handles files without extensions by placing them in a `no_extension` directory.

## Usage

1. **Clone or download the script:**

   Download the script file (`organize_files.py`) from the repository or clone the repository if applicable.

2. **Set up the script:**

   Open the script file and replace `'directory_path'` with the path to the directory you want to organize.

   ```python
   organize_files('directory_path')
