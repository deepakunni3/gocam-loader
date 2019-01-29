import logging
from rdflib.namespace import RDF, RDFS
from rdflib import Graph
from rdflib.term import Node, BNode, Literal, URIRef
from prefixcommons import curie_util
from bidict import bidict


prefix_map = curie_util.read_biocontext("go_context")

def is_BNode(node: Node):
    return isinstance(node, BNode)

def is_Literal(node: Node):
    return isinstance(node, Literal)

def is_URIRef(node: Node):
    return isinstance(node, URIRef)

def labels(graph: Graph, node: Node):
    results = None
    if not is_BNode(node):
        results = [o for o in graph.objects(node, RDFS.label)]
    return results

def short_label(uri: URIRef):
    curie = curie_util.contract_uri(uri, prefix_map, strict=True)
    if len(curie) == 0:
        logging.warning("contract_uri failed for URI {}".format(uri))
        # TODO: replace '_' in curie with ':'
        curie = uri.split('/')[-1]
    return curie

def types(graph: Graph, node: Node, include_individual: bool):
    results = None
    if not is_BNode(node):
        results = [o for o in graph.objects(node, RDF.type)]
    return results


CAUSAL_RELATIONS = bidict({
    "enabled_by": "http://purl.obolibrary.org/obo/RO_0002333",
    "occurs_in": "http://purl.obolibrary.org/obo/BFO_0000066",

    "has_input": "http://purl.obolibrary.org/obo/RO_0002233",
    "has_output": "http://purl.obolibrary.org/obo/RO_0002234",

    "part_of": "http://purl.obolibrary.org/obo/BFO_0000050",
    "has_part": "http://purl.obolibrary.org/obo/BFO_0000051",

    "directly_activates": "http://purl.obolibrary.org/obo/RO_0002406",
    "directly_inhibits": "http://purl.obolibrary.org/obo/RO_0002408",

    "directly_provides_input_for": "http://purl.obolibrary.org/obo/RO_0002413",
    "directly_positively_regulates": "http://purl.obolibrary.org/obo/RO_0002629",
    "directly_negatively_regulates": "http://purl.obolibrary.org/obo/RO_0002630",

    "causally_upstream_of": "http://purl.obolibrary.org/obo/RO_0002411",
    "causally_upstream_of_positive_effect": "http://purl.obolibrary.org/obo/RO_0002304",
    "causally_upstream_of_negative_effect": "http://purl.obolibrary.org/obo/RO_0002305",

    "causally_upstream_of_or_within": "http://purl.obolibrary.org/obo/RO_0002418",
    "causally_upstream_of_or_within_positive_effect": "http://purl.obolibrary.org/obo/RO_0004047",
    "causally_upstream_of_or_within_negative_effect": "http://purl.obolibrary.org/obo/RO_0004046",

    "positively_regulates": "http://purl.obolibrary.org/obo/RO_0002213",
    "negatively_regulates": "http://purl.obolibrary.org/obo/RO_0002212",

    "results_in_acquisition_of_features_of": "http://purl.obolibrary.org/obo/RO_0002315",
    "transports_or_maintains_localization_of": "http://purl.obolibrary.org/obo/RO_0002313",
    "results_in_movement_of": "http://purl.obolibrary.org/obo/RO_0002565"
})

RDFS = bidict({
    "label": "http://www.w3.org/2000/01/rdf-schema#"
})

RDF = bidict({
    "type": "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
})

OWL = bidict({
    "individual": "http://www.w3.org/2002/07/owl#NamedIndividual"
})
