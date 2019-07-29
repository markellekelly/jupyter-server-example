import os
import jinja2
from jupyter_server.extension.application import ExtensionApp
from .handler import MyExtHandler

HERE = os.path.dirname(__file__)

class MyExt(ExtensionApp):
    
  # Name of the extension
  extension_name = "my_ext"

  # Local path to static files directory.
  static_paths = [
    os.path.join(HERE,'static')
  ]

  # Local path to templates directory.

  def initialize_templates(self):
    mypath = os.path.join(HERE,'templates')
    print(mypath)
    template_paths = [
      mypath
    ]
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_paths))
    template_settings={'myext_jinja2_env':env}
    self.settings.update(**template_settings)

  def initialize_handlers(self):
    self.handlers.append(
      (r'/myext/(.*)', MyExtHandler)
    )

main = MyExt.launch_instance