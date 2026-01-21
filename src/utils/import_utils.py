import importlib.util


class ImportUtils:
    @staticmethod
    def import_module_from_path(module_name: str, file_path: str):
        spec = importlib.util.spec_from_file_location(
            module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)  # type: ignore
        return module
