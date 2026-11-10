import os
import shutil

folder_path = '/sdcard/Download'

# تعريف المجلدات والامتدادات الخاصة بكل نوع
extensions = {
    'Images': ('.jpg', '.jpeg', '.png', '.gif'),
    'Documents': ('.pdf', '.docx', '.doc', '.txt', '.xlsx', '.mht'),
    'Audio': ('.mp3', '.oga', '.wav', '.m4a'),
    'Videos': ('.mp4', '.mkv', '.avi')
}

try:
    files = os.listdir(folder_path)
    print("Files found:", files)
    
    for file in files:
        file_path = os.path.join(folder_path, file)
        
        # تخطي المجلدات حتى لا ينقل مجلداً داخل مجلد آخر
        if os.path.isdir(file_path):
            continue
            
        file_lower = file.lower()
        
        # فحص نوع الملف ونقله للمجلد المناسب
        for folder_name, exts in extensions.items():
            if file_lower.endswith(exts):
                target_folder = os.path.join(folder_path, folder_name)
                
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                    
                shutil.move(file_path, os.path.join(target_folder, file))
                print(f"Moved {file} to {folder_name}")
                break
                
    print("Done organizing all files successfully!")
except Exception as e:
    print("Error:", e)
