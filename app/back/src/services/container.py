import docker
from typing import TextIO

class Container:
    def __init__(self):
        self.client = docker.from_env()
        

    async def build_from_text(self, docker_file_path: str, tag: str):
        
        print("começou o build")
        print(docker_file_path)
        image, build_logs = self.client.images.build(path=docker_file_path, tag=tag, dockerfile="./Dockerfile", rm=True)
        for log in build_logs:
            print(log)
        
        self.client.containers.run(image=image, ports={'80/tcp':80}, detach=True)
     