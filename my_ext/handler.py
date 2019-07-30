from jupyter_server.extension.handler import ExtensionHandler

class MyExtHandler(ExtensionHandler):
    
    def get_template(self,name):
        return self.settings['myext_jinja2_env'].get_template(name)

    def get(self):
        base_url = self.settings.get('base_url')
        # pass base url (to find .js) to html file
        html = self.render_template("index.html", base_url=base_url)
        self.write(html)


class MyExtHandler2(ExtensionHandler):
    
    def get_template(self,name):
        return self.settings['myext_jinja2_env'].get_template(name)

    def get(self, path):
        base_url = self.settings.get('base_url')
        #pass input text (path) to the html file
        html = self.render_template("page1.html", text=path)
        self.write(html)

class ErrorHandler(ExtensionHandler):
    
    def get_template(self,name):
        return self.settings['myext_jinja2_env'].get_template(name)

    def get(self, path):
        html = self.render_template("error.html")
        self.write(html)