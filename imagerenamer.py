import os
import logging

def get_user_input(prompt):
    return input(prompt)

def validate_folder(folder_path):
    return os.path.exists(folder_path)

def filter_image_files(all_files, case_sensitive):
    extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff']
    if case_sensitive:
        return [f for f in all_files if any(f.endswith(ext) for ext in extensions)]
    else:
        return [f for f in all_files if any(f.lower().endswith(ext) for ext in extensions)]

def rename_files(folder_path, prefix, image_files, skip_existing):
    total_files = len(image_files)
    counter = 1
    for img in image_files:
        # Progress Feedback
        print(f"Progress: {counter}/{total_files} ({(counter / total_files) * 100:.2f}%)")
        
        extension = os.path.splitext(img)[1]
        new_name = f"{prefix}{str(counter).zfill(3)}{extension}"
        old_path = os.path.join(folder_path, img)
        new_path = os.path.join(folder_path, new_name)
        
        if os.path.exists(new_path):
            logging.warning(f"File {new_name} already exists.")
            if skip_existing:
                logging.info("Skipping.")
                counter += 1
                continue
            else:
                logging.info("Overwriting.")

        try:
            os.rename(old_path, new_path)
            logging.info(f"Renamed {img} to {new_name}")
        except PermissionError:
            logging.error(f"Permission error: Could not rename {img} to {new_name}.")
        except Exception as e:
            logging.error(f"An error occurred while renaming {img} to {new_name}. Error: {e}")
        counter += 1

def rename_images_in_folder():
    logging.basicConfig(level=logging.INFO)

    folder_path = get_user_input("Enter the folder path where the images are stored: ")
    
    if not validate_folder(folder_path):
        logging.error("The specified folder does not exist.")
        return

    prefix = get_user_input("Enter the prefix string for renaming the files: ")
    case_sensitive = get_user_input("Consider file extensions case-sensitive? (yes/no): ") == 'yes'
    skip_existing = get_user_input("Skip existing files? (yes/no): ") == 'yes'

    all_files = os.listdir(folder_path)
    image_files = filter_image_files(all_files, case_sensitive)

    if len(image_files) == 0:
        logging.warning("No image files found to rename.")
        return

    confirm = get_user_input(f"{len(image_files)} image files will be renamed. Do you want to continue? (yes/no): ")
    if confirm.lower() != 'yes':
        logging.info("Operation cancelled by the user.")
        return

    rename_files(folder_path, prefix, image_files, skip_existing)

# Call the function to rename images
rename_images_in_folder()
