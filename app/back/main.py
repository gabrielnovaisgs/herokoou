from fastapi import FastAPI
from src.models import Template

app = FastAPI()

@app.get('/')
def read_root():
    template = Template()
    docker_template = template.fill_docker_template()
    
    return {'Hello': 'World'}

