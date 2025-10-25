from jinja2 import Environment, PackageLoader, select_autoescape

class Template:
    
    def __init__(self):
        self.env = Environment(
            loader=PackageLoader('src'),
            autoescape=select_autoescape()
        )  

    def fill_docker_template(self):
        template = self.env.get_template("dockerfiles/nginx.dockerfile")
        html=self.env.get_template("index.html")
        return template.render(html=html.render())
        