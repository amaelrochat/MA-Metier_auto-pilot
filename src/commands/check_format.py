from src.format import PythonFormatter


def check_format(args):
    formatter = PythonFormatter()
    return_code = 0

    for file_path in formatter.check():
        print(f"File {file_path} is not properly formatted.")
        return_code = 1

    return return_code
