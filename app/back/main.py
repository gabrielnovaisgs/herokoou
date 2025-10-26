from fastapi import FastAPI
from back.src.services import Template, Container
from back.src.models import User, Build
app = FastAPI()

@app.get('/')
async def read_root():
    user = User("asd")
    build = Build("hjkjj")
    template = Template(user)
    docker_template = template.build_docker_file_html(build)
    container_service = Container()
    await container_service.build_from_text(docker_file_path=docker_template, tag="teste:1")
    return {'Hello': 'World'}

