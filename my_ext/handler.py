from jupyter_server.extension.handler import ExtensionHandler

class MyExtHandler(ExtensionHandler):
    
  def get_template(self,name):
    return self.settings['myext_jinja2_env'].get_template(name)

  def get(self, path):
    if path=="page1":
      html = self.render_template("page1.html")
      self.write(html)
    else:
      html = self.render_template("index.html")
      self.write(html)