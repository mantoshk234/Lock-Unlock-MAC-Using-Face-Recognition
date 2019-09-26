import os


def assure_clean_path_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        return
    else:  # if directory exists, delete all its content
        filePaths = [os.path.join(dir_path, f) for f in os.listdir(dir_path)]  # Get all file path
        for file_path in filePaths:
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception:
                pass
