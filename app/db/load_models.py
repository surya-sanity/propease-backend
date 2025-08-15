import pkgutil
import importlib
import app.models


def load_models():
    package = app.models
    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        importlib.import_module(f"{package.__name__}.{module_name}")
