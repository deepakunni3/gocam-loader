from gocam_loader.io.parser import Parser
import gocam_loader.util.utils as Utils
import rdflib

class TtlParser(Parser):

    def __init__(self, **args: dict):
        super().__init__()

    def parse_graph(self, graph: rdflib.Graph):
        for subject, pred, object in graph:
            pass