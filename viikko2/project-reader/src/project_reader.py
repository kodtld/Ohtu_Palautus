from urllib import request
from project import Project
from toml import dumps,loads,dump


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        new_content = loads(content)
        name = new_content['tool']['poetry']['name']
        desc = new_content['tool']['poetry']['description']
        depends = new_content['tool']['poetry']['dependencies']
        dev_depends = new_content['tool']['poetry']['dev-dependencies']

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, depends, dev_depends)
