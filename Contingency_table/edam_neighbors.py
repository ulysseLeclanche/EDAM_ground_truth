from SPARQLWrapper import SPARQLWrapper, JSON


endpointURL = "http://localhost:3030/biotoolsEdam/query"
rdfFormat = "turtle"

prefixes = """
PREFIX edam: <http://edamontology.org/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
"""

prefixes = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>

PREFIX bt: <https://bio.tools/>
PREFIX biotools: <https://bio.tools/ontology/>
PREFIX bsc: <http://bioschemas.org/>
PREFIX bsct: <http://bioschemas.org/types/>
PREFIX edam: <http://edamontology.org/>
PREFIX sc: <http://schema.org/>
PREFIX schema: <https://schema.org/>

"""

biotoolsURI = "https://bio.tools/"
biotoolsOntologyURI = "https://bio.tools/ontology/"
edamURI = "http://edamontology.org/"

def get_edam_neighbors(uri_list):
    """
    Retrieve EDAM neighbors for a list of EDAM URIs.
    """

    annotation_neighbors = set()

    for uri in uri_list:

        currentAnnotation = uri.replace(edamURI, "edam:")
        annotation_neighbors.add(uri)

        query = f"""
SELECT DISTINCT ?neighbor ?neighborLabel
WHERE {{
  VALUES ?conceptRoot {{ 
    edam:topic_0003
    edam:operation_0004
    edam:data_0006
    edam:format_1915
  }}

  VALUES ?neighborRoot {{ 
    edam:topic_0003
    edam:operation_0004
    edam:data_0006
    edam:format_1915
  }}

  VALUES ?concept {{ {currentAnnotation} }}

  ?concept rdfs:subClassOf* ?conceptRoot .
  ?concept rdf:type owl:Class .
  FILTER NOT EXISTS {{ ?concept rdfs:subClassOf owl:DeprecatedClass }}

  {{
  ?concept (rdfs:subClassOf|owl:someValuesFrom)* [
    rdf:type owl:Restriction ;
    owl:onProperty ?relation ;
    owl:someValuesFrom ?neighborDescendant
  ] .
  }}
  UNION 
  {{
  ?concept rdfs:subClassOf ?neighborDescendant .
  ?concept ?relation ?neighborDescendant .
  }}

  ?neighborDescendant rdfs:subClassOf* ?neighbor .

  ?neighbor rdfs:subClassOf* ?neighborRoot .
  ?neighbor rdf:type owl:Class .
  FILTER NOT EXISTS {{ ?neighbor rdfs:subClassOf owl:DeprecatedClass }}
  OPTIONAL {{ ?neighbor rdfs:label ?neighborLabel . }}
}}
"""

        sparql = SPARQLWrapper(endpointURL)
        sparql.setQuery(prefixes + query)
        sparql.setReturnFormat(JSON)

        results = sparql.queryAndConvert()

        for result in results["results"]["bindings"]:
            annotation_neighbors.add(result["neighbor"]["value"])

    return list(annotation_neighbors)