import os

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):


    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))
        if os.path.commonpath([abs_working_dir, target_file]) != abs_working_dir:
            return f'Error: Cannot access "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(target_file, 'r', encoding='utf-8', errors='replace') as file:
            content = file.read(MAX_CHARS)
            extra = file.read(1)
            if extra != '':
                return f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content
    except Exception as e:
        return f"Error reading file: {e}"