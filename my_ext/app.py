import os
import jinja2
from jupyter_server.extension.application import ExtensionApp
from .handler import MyExtHandler, MyExtHandler2, ErrorHandler

HERE = os.path.dirname(__file__)

class MyExt(ExtensionApp):
    
    # Name of the extension.
    extension_name = "my_ext"

    # Local path to static files directory.
    static_paths = [ os.path.join(HERE,'static') ]

    # Default to the extension's URL.
    default_url = "/myext"

    def initialize_templates(self):
        # Local path to templates directory.
        template_paths = [os.path.join(HERE,'templates')]
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_paths))
        template_settings={'myext_jinja2_env':env}
        self.settings.update(**template_settings)

    def initialize_handlers(self):
        # Add a group with () to send to handler.
        self.handlers.extend([
            (r'/myext/?', MyExtHandler),
            (r'/myext/page1/(.*)', MyExtHandler2),
            (r'/myext/(.*)', ErrorHandler)
        ])
                    
main = MyExt.launch_instance