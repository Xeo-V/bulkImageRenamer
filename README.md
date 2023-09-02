# bulkImageRenamer
Bulk Image Renamer  This Python script automatically renames all image files in a specified folder with a user-defined prefix and sequential numbering (e.g., "Prefix_001.jpg").
-----------------------------------------------------------------------------------------------------------------------------

Description

The Bulk Image Renamer is a Python script designed to automatically rename all image files in a specified directory. Files are renamed according to a user-defined prefix and are sequentially numbered (e.g., "Prefix_001.jpg").
Use Cases

    Photography: Renaming batches of photos from a shoot for easier organization.
    Game Development: Renaming asset files for integration into game engines.
    Machine Learning: Renaming image datasets for easier parsing and analysis.
    General File Management: Any situation where uniform file naming is needed.
-----------------------------------------------------------------------------------------------------------------------------

How to Use

    Clone this repository or download the Python script.
    Open a terminal and navigate to the folder where the script is located.
    Run the script by executing python rename_images.py (Python 3.x is required).
    When prompted, enter the full path of the folder containing the images you wish to rename.
    Enter the prefix string that you want to use for renaming the files.

Example:

Enter the folder path where the images are stored: /path/to/image/folder
Enter the prefix string for renaming the files: MyPrefix_
-----------------------------------------------------------------------------------------------------------------------------

Requirements

    Python 3.x
    No external modules are needed; the script uses Python's built-in os library.
-----------------------------------------------------------------------------------------------------------------------------

Features

    Supports common image formats including .png, .jpg, .jpeg, .gif, .bmp, and .tiff.
    Automatically numbers files starting from 001.
    Skips non-image files in the directory.
-----------------------------------------------------------------------------------------------------------------------------

Limitations

    Currently supports only a limited set of image formats. You may extend this by modifying the code.
-----------------------------------------------------------------------------------------------------------------------------
License : 

This project is open-source and available under the MIT License.
