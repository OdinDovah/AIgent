import os


def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
        return f"Error: Cannot read '{file_path}' as it is outside the permitted working directory"
    if not os.path.isfile(full_path):
        return f"Error: File not found or is not a regular file: '{file_path}'"
    try:
        with open(full_path) as f:
            contents = f.read()
            if len(contents) > 10000:
                return contents[:10000] + f"\n[...File '{file_path}' truncated at 10000 characters]"
            return contents
    except Exception as e:
        return f"Error: {str(e)}"
