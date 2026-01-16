from src.format import PythonFormatter


def format(args):
    formatter = PythonFormatter()

    for file_path in formatter.format():
        print(f"Formatted: {file_path}")

    return 0
