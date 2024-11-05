from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print("*", content, "*")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        content = toml.loads(content)
        name = content["tool"]["poetry"]["name"]
        description = content["tool"]["poetry"]["description"]
        dependencies = content["tool"]["poetry"]["dependencies"].keys()
        dev_dependencies = content["tool"]["poetry"]["group"]["dev"]["dependencies"].keys()
        authors = content["tool"]["poetry"]["authors"]
        license = content["tool"]["poetry"]["license"]
        return Project(name, description, dependencies, dev_dependencies, authors, license)
