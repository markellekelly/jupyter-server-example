from setuptools import setup

setup(
    name='my_ext',
    version='0.1',
    data_files=[
        ('etc/jupyter/jupyter_server_config.d', ['etc/jupyter/jupyter_server_config.d./my_extension.json']),
    ],
    entry_points= {
        'console_scripts': [
             'jupyter-myext = my_ext.app:main'
        ]
    },
)