from src.utils.import_utils import ImportUtils


def http(args):
    ImportUtils.import_module_from_path(
        "bootstrap", "./src/http/bootstrap.py")
