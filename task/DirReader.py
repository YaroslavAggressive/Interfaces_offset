import os

LINE_SEPARATOR = "\\"

class DirReader:

    def __init__(self, dir_path):
        self.dir_path = dir_path


    def find_correct_files(self, dir_path):
        for sub_dir, dirs, files in os.walk(dir_path):
            for file in files:
                path, format = os.path.splitext(file)
                if format == ".txt":
                    yield sub_dir + LINE_SEPARATOR + path + format

    def __enter__(self):
        return self.find_correct_files(self.dir_path)


    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
