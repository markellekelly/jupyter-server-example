from .app import MyExt

EXTENSION_NAME = "my_ext"

def _jupyter_server_extension_paths():
    return [{"module": EXTENSION_NAME}]

load_jupyter_server_extension = MyExt.load_jupyter_server_extension