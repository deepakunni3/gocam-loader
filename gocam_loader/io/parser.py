import urllib.request
import rdflib


class Parser:

    def __init__(self, **args: dict):
        pass

    def read_from_file(self, file: str):
        g = rdflib.Graph()
        g.parse(file, format='ttl')
        self.parse_graph(g)

    def read_from_remote_file(self, file_url: str):
        local_filename, headers = urllib.request.urlretrieve(file_url)
        g = rdflib.Graph()
        g.parse(local_filename, format='ttl')
        self.parse_graph(g)

    def parse_graph(self, g: rdflib.Graph):
        raise NotImplementedError()
