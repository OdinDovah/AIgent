import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
        return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"
    if not os.path.isdir(full_path):
        return f"Error: '{directory}' is not a directory"
    dir_contents = []
    try:
        all_contents = os.listdir(full_path)
        for content in all_contents:
            content_path = os.path.join(full_path, content)
            dir_contents.append(f"- {content}: file_size={os.path.getsize(content_path)} bytes, is_dir={os.path.isdir(content_path)}")
        return "\n".join(dir_contents)
    except Exception as e:
        return f"Error: {str(e)}"
