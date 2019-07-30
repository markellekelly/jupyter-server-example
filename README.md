# jupyter-server-example
Simple example of creating a server extension using the new Jupyter server. This allows you to put your own frontend on a Jupyter server, giving you access to the whole Jupyter REST API. You also can add HTML templates and link your TypeScript to the server.
When an extension application is launched, it
1. starts and launches an instance of the Jupyter server.
2. calls `self.load_jupyter_server_extension()` method.
3. loads configuration from config files+command line.
3. appends the extension's handlers to the main web application.
4. appends a `/static/<extension_name>/` endpoint where it serves static files (i.e. js, css, etc.).

## Steps
1. Subclass the `ExtensionApp`. Set the following traits:
    * `extension_name`: name of the extension.
    * `static_paths`: path to static files directory
    * `template_paths`: path to templates directory.
    
    and define the following methods:
    * `initialize_handlers()`: append handlers to `self.handlers` in tuples of (r'/mypath/', MyHandlerName)
    * `initialize_settings()`: add extensions settings to the webapp using `self.settings`.
    * `initialize_templates()`: setup your HTML templating options.

    **Example using jinja for HTML templating**
    ```python
    # application.py
    from jupyter_server.extension.application import ExtensionApp

    class MyExtension(ExtensionApp):
        
        # Name of the extension
        extension_name = "my_extension"
        
        # Local path to static files directory.
        static_paths = [
            "/path/to/static/dir/"
        ]

        # Local path to templates directory.
        template_paths = [
            "/path/to/template/dir/"
        ]

        def initialize_handlers(self):
            self.handlers.append(
                (r'/myextension', MyExtensionHandler)
            )

        def initialize_templates(self):
            template_paths = [os.path.join(HERE,'templates')]
            env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_paths))
            template_settings={'myextension_jinja2_env':env}
            self.settings.update(**template_settings)

        def initialize_settings(self):
            ...

    ```

2. Define handlers by subclassing the `ExtensionHandler`. 

    **Example using jinja**
    ```python
    # handler.py
    from jupyter_server.extension.handler import ExtensionHandler

    class MyExtensionHandler(ExtensionHandler):
    
        def get_template(self,name):
            return self.settings['myextension_jinja2_env'].get_template(name)
        
        def get(self):
            html = self.render_template("index.html")
            self.write(html)
    ```


3. Point Jupyter server to the extension. We need to define two things:
    * `_jupyter_server_extension_paths()`: a function defining what module to load the extension from.
    * `load_jupyter_server_extension()`: point there server to the extension's loading function mechansim.

    **Example**
    ```python
    # __init__.py
    from .extension import MyExtension


    EXTENSION_NAME = "my_extension"

    def _jupyter_server_extension_paths():
        return [{"module": EXTENSION_NAME}]

    load_jupyter_server_extension = MyExtension.load_jupyter_server_extension
    ```

4. Add the following configuration to your jupyter configuration directory to enable the extension.

    ```json
    {
      "ServerApp": {
        "jpserver_extensions": {
          "notebook": true
        }
      }
    }
    ```
    
5. Add entry point in `setup.py`.

    ```python
    setup(
        name='my_extension',
        version='0.1',
        data_files=[
            ('etc/jupyter/jupyter_server_config.d', ['etc/jupyter/jupyter_server_config.d./my_extension.json']),
        ],
        ...
        'entry_points': {
            'console_scripts': [
                 'jupyter-myext = my_extension.application:MyExtension.launch_instance'
            ]
        },
        ...
    )
    ```

**How do I pass in my JavaScript?**
1. In your extension handler, pass the base_url to your template.
```python
def get(self):
        base_url = self.settings.get('base_url')
        html = self.render_template("index.html", base_url=base_url)
        ...
```
2. In your HTML template file, reference your bundled JavaScript in a `<script>`.
```html
    <script src="{{static_url('bundle.js')}}" type="text/javascript" charset="utf-8"></script>
```
