from back.src.models import User, Build

from jinja2 import Environment, PackageLoader, select_autoescape
from os.path import join
from os import getcwd, makedirs
import os

from shutil import copyfile

class Template:
    tmp_directory: str
    template_path = join(getcwd(),'src', 'templates')
    user: User

    def __init__(self, user: User):
        self.user = user

        self.env = Environment(
            loader=PackageLoader('back.src'),
            autoescape=select_autoescape()
        )


    def build_docker_file_html(self, build: Build)-> str:
        self._create_temp_path(build=build)
        copyfile(join(self.template_path, 'dockerfiles', 'nginx.dockerfile'), join(self.tmp_directory, 'Dockerfile'))
        
        
        html_template=self.env.get_template("index.html")
        render_template = html_template.render({
            'user': self.user.id
        })
        self._save_tmp_file(file_name='index.html',file_content= render_template )
        return self.tmp_directory
    
    
    def _create_temp_path(self, build: Build) -> str:
        self.tmp_directory = join(getcwd(),'tmp', self.user.id, build.id)
        if not os.path.exists(self.tmp_directory):
            makedirs(self.tmp_directory)
    
    def _save_tmp_file(self, file_name: str, file_content: str):
        file_full_path: str = join(self.tmp_directory, file_name)
        with open(file_full_path, 'w') as file:
            file.write(file_content)