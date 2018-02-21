## Introduction
This is the old storage location of the SNIK ontology RDF dump. The official SPARQL Endpoint http://www.snik.eu/sparql contains the current version, which is shown in the graph visualization http://www.snik.eu/graph. Changes to these files here will not influence the contents of the SPARQL endpoint, use the OntoWiki at http://www.snik.eu/ontowiki for that.

## Components

| Subontology | Name | Source | Comments |
|---|---|-----|---|
|meta.rdf	|Meta	| Hand-crafted |	Defines general terms. |
|bb.rdf		|Blue Book | Health Information Systems, A. Winter et al. |
|ob.rdf		|Orange Book |IT-Projektmanagement im Gesundheitswesen, E. Ammenwerth et al. ||
|ciox.rdf	| CIOX | Hospital Interviews | Licensing not clear thus not available yet. |

## Editing

* Edit only with a text editor.
* Please make sure that you produce the smallest diff possible for your changes, e.g. don't use a tool that shuffles the definition locations around or changes line endings or indentation.
* Verify after editing with:
```
xmllint --noout filename.rdf
rapper -i rdfxml -c filename.rdf
````

## Filling your own SPARQL Endpoint

1. Go to “Linked Data”->"Quad Store Upload” and upload the files. If an RDF/XML serialized file (*.rdf) does not work, convert it to ntriples and upload that.

|File| Graph|
|---|----|
|meta.rdf	|http://www.snik.eu/ontology/meta|
|bb.rdf 	|http://www.snik.eu/ontology/bb|
|links_bb.ttl |	http://www.snik.eu/ontology/bb|
|ob.rdf 	|http://www.snik.eu/ontology/ob|
|ciox.rdf |	http://www.snik.eu/ontology/ciox|
|links_ciox.rdf |	http://www.snik.eu/ontology/ciox|

Check if it worked by querying `select count(*) {?s ?p ?o.}` for each graph.

2. Add graphs to graph group

```
DB.DBA.RDF_GRAPH_GROUP_INS ('http://www.snik.eu/ontology', 'http://www.snik.eu/ontology/bb');
DB.DBA.RDF_GRAPH_GROUP_INS ('http://www.snik.eu/ontology', 'http://www.snik.eu/ontology/ob');
DB.DBA.RDF_GRAPH_GROUP_INS ('http://www.snik.eu/ontology', 'http://www.snik.eu/ontology/meta');
DB.DBA.RDF_GRAPH_GROUP_INS ('http://www.snik.eu/ontology', 'http://www.snik.eu/ontology/ciox');
```

3. (Optional) Add virtual Triples
   1. Query `sparql/construct_virtual_triples_and_missing.sparql.txt` as N-Triples
   2. Upload the result to the graph `http://www.snik.eu/ontology/virtual`

## License
Because we extracted the triples from copyrighted books with permission of the publishers, we chose a noncommercial license with copyleft, the *Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International*, see LICENCE for details.
We want to encourage reuse, modification, derivation and distribution as much as possible, so if that license is a problem for you please contact [Prof. Winter](www.people.imise.uni-leipzig.de/alfred.winter) and we try our best to find a solution.
