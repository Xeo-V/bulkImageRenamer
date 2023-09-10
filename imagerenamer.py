import os
import logging
import json

def load_localization(language_code):
    try:
        with open(f'localization/{language_code}.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error(f"Localization file for {language_code} not found. Falling back to English.")
        with open('localization/en.json', 'r', encoding='utf-8') as f:
            return json.load(f)

def get_user_input(prompt):
    return input(prompt)

def validate_folder(folder_path):
    return os.path.exists(folder_path)

def filter_image_files(all_files):
    return [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'))]

def rename_files(folder_path, prefix, localization):
    all_files = os.listdir(folder_path)
    image_files = filter_image_files(all_files)
    total_files = len(image_files)
    counter = 1
    undo_mapping = {}
    
    for img in image_files:
        extension = os.path.splitext(img)[1]
        new_name = f"{prefix}{str(counter).zfill(3)}{extension}"
        old_path = os.path.join(folder_path, img)
        new_path = os.path.join(folder_path, new_name)
        
        if os.path.exists(new_path):
            logging.warning(f"File {new_name} already exists. Skipping.")
            continue
        
        os.rename(old_path, new_path)
        logging.info(f"Renamed {img} to {new_name}")
        
        undo_mapping[old_path] = new_path
        counter += 1

    undo_file_path = os.path.join(folder_path, "undo_mapping.json")
    with open(undo_file_path, 'w') as f:
        json.dump(undo_mapping, f)
    logging.info(localization['undo_saved'] + undo_file_path)

def rename_images_in_batch():
    logging.basicConfig(level=logging.INFO)
    
    # Load localization
    language_code = get_user_input("Select language (en, es, etc.): ")
    localization = load_localization(language_code)
    
    folder_paths_str = get_user_input(localization['folder_prompt'])
    folder_paths = folder_paths_str.split(',')

    for folder_path in folder_paths:
        folder_path = folder_path.strip()
        if not validate_folder(folder_path):
            logging.error(f"The specified folder does not exist: {folder_path}")
            continue

        prefix = get_user_input(localization['prefix_prompt'])
        rename_files(folder_path, prefix, localization)

# Call the function to rename images in batch
rename_images_in_batch()
