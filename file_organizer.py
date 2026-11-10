import os
import shutil

folder_path = '/sdcard/Download'

try:
    files = os.listdir(folder_path)
    print("Files found:", files)
    
    for file in files:
        if file.lower().endswith(('.jpg', '.png', '.jpeg')):
            target_folder = os.path.join(folder_path, 'Images')
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            shutil.move(os.path.join(folder_path, file), os.path.join(target_folder, file))
            print("Moved:", file)
            
    print("Done successfully!")
except Exception as e:
    print("Error:", e)
