import re

props = [
['http://www.snik.eu/ontology/bb/Chapter','http://www.snik.eu/ontology/bb/chapter'],
['http://www.snik.eu/ontology/bb/ConceptDomain','http://www.snik.eu/ontology/bb/conceptDomain'],
['http://www.snik.eu/ontology/bb/ID','http://www.snik.eu/ontology/bb/id'],
['http://www.snik.eu/ontology/bb/TripelPage','http://www.snik.eu/ontology/bb/tripelPage'],
['http://www.snik.eu/ontology/bb/TripelRowNr','http://www.snik.eu/ontology/bb/tripelRowNr'],
['http://www.snik.eu/ontology/it4it/Chapter','http://www.snik.eu/ontology/it4it/chapter'],
['http://www.snik.eu/ontology/it4it/MainFunctions','http://www.snik.eu/ontology/it4it/mainFunctions'],
['http://www.snik.eu/ontology/it4it/OntologyDomain','http://www.snik.eu/ontology/it4it/ontologyDomain'],
['http://www.snik.eu/ontology/it4it/OntologyQuestionTypes','http://www.snik.eu/ontology/it4it/ontologyQuestionTypes'],
['http://www.snik.eu/ontology/it4it/OntologyUse','http://www.snik.eu/ontology/it4it/ontologyUse'],
['http://www.snik.eu/ontology/it4it/OntologyUser','http://www.snik.eu/ontology/it4it/ontologyUser'],
['http://www.snik.eu/ontology/it4it/Purpose','http://www.snik.eu/ontology/it4it/purpose'],
['http://www.snik.eu/ontology/meta/DefinitionDEPage','http://www.snik.eu/ontology/meta/definitionDePage'],
['http://www.snik.eu/ontology/ob/Chapter','http://www.snik.eu/ontology/ob/chapter'],
['http://www.snik.eu/ontology/ob/ConceptDomain','http://www.snik.eu/ontology/ob/conceptDomain'],
['http://www.snik.eu/ontology/ob/ID','http://www.snik.eu/ontology/ob/id'],
['http://www.snik.eu/ontology/ob/TripelPage','http://www.snik.eu/ontology/ob/tripelPage'],
['http://www.snik.eu/ontology/ob/TripelRowNr','http://www.snik.eu/ontology/ob/tripelRowNr']
]

for entry in props:
    wrong, correct = entry 
    graph = re.sub(r"/[^/]*$","",wrong)
    subjectQuery = fr"""SPARQL
    with <{graph}>
    delete
    {{
    ?s ?p <{wrong}> .
    }}
    insert
    {{
    ?s ?p <{correct}> .
    }}
    where
    {{
    ?s ?p <{wrong}> .
    }}"""
    
    predicateQuery = fr"""SPARQL
    with <{graph}>
    delete
    {{
    ?s <{wrong}> ?o .
    }}
    insert
    {{
    ?s <{correct}> ?o.
    }}
    where
    {{
    ?s <{wrong}> ?o.
    }}"""

    objectQuery = fr"""SPARQL
    with <{graph}>
    delete
    {{
    <{wrong}> ?p ?o .
    }}
    insert
    {{
    <{correct}> ?p ?o.
    }}
    where
    {{
    <{wrong}> ?p ?o.
    }}"""

    print(subjectQuery)
    print("")
    print(predicateQuery)
    print("")
    print(objectQuery)
    print("")
