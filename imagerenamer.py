import os

def rename_images_in_folder():
    # Ask the user for the folder path
    folder_path = input("Enter the folder path where the images are stored: ")
    
    # Validate if the folder exists
    if not os.path.exists(folder_path):
        print("The specified folder does not exist.")
        return
    
    # Ask the user for the prefix string to use for renaming
    prefix = input("Enter the prefix string for renaming the files: ")
    
    # List all the files in the folder
    all_files = os.listdir(folder_path)
    
    # Filter only image files (you can add more image extensions if needed)
    image_files = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'))]
    
    # Sort the image files to keep numbering consistent
    image_files.sort()
    
    # Initialize a counter for numbering
    counter = 1
    
    for img in image_files:
        # Create the new name
        new_name = f"{prefix}{str(counter).zfill(3)}.jpg"
        
        # Create the full path for the current and new file names
        old_path = os.path.join(folder_path, img)
        new_path = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed {img} to {new_name}")
        
        # Increment the counter
        counter += 1

# Call the function
rename_images_in_folder()
