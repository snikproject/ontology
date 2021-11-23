# SNIK Ontology

SNIK is an ontology of information management in hospitals.

## See Also

* [Project Homepage](https://www.snik.eu/)
* [RDF Browser](https://www.snik.eu/ontology)
* [SPARQL Endpoint](https://www.snik.eu/sparql)
* [Graph Visualization](https://www.snik.eu/graph)

## Components

| Subontology | Name | Source | Comments |
|---|---|-----|---|
|meta.ttl	|Meta	| Hand-crafted |	Defines general terms. |
|bb.ttl		|Blue Book | Health Information Systems, A. Winter et al. |
|ob.ttl		|Orange Book |IT-Projektmanagement im Gesundheitswesen, E. Ammenwerth et al. ||
|he.ttl	|  Heinrich| Informationsmanagement: Grundlagen Aufgaben Methoden, L.J. Heinrich et al. ||
|ciox.ttl	| CIOX | Hospital Interviews ||
|it4it.ttl	| IT4IT | Standard||

## Editing

* Edit only with a text editor.
* Please make sure that you produce the smallest diff possible for your changes, e.g. don't use a tool that shuffles the definition locations around or changes line endings or indentation.
* Verify after editing with:
    
    rapper -i turtle -c filename.ttl

## Filling your own SPARQL Endpoint
If you do not need the graph group and subgraphs, you can run `scripts/combine` to merge everything into one file `/tmp/snik.ttl`, which you an upload to the graph `http://www.snik.eu/ontology`, otherwise:

1. Go to “Linked Data”->"Quad Store Upload” and upload the files.

|File| Graph|
|---|----|
|meta.ttl	|http://www.snik.eu/ontology/meta|
|bb.ttl 	|http://www.snik.eu/ontology/bb|
|ob.ttl 	|http://www.snik.eu/ontology/ob|
|ciox.ttl   |http://www.snik.eu/ontology/ciox|
|it4it.ttl   |http://www.snik.eu/ontology/it4it|
|limes.nt   |http://www.snik.eu/ontology/limes-exact|
|match.nt   |http://www.snik.eu/ontology/match|

Check if it worked by querying `select count(*) {?s ?p ?o.}` for each graph.

2. Add graphs to graph group in the Virtuoso Conductor ISQL panel

	DB.DBA.RDF_GRAPH_GROUP_CREATE('http://www.snik.eu/ontology');
    DB.DBA.RDF_GRAPH_GROUP_INS ('http://www.snik.eu/ontology', 'http://www.snik.eu/ontology/bb');
    DB.DBA.RDF_GRAPH_GROUP_INS ('http://www.snik.eu/ontology', 'http://www.snik.eu/ontology/ob');
    DB.DBA.RDF_GRAPH_GROUP_INS ('http://www.snik.eu/ontology', 'http://www.snik.eu/ontology/meta');
    DB.DBA.RDF_GRAPH_GROUP_INS ('http://www.snik.eu/ontology', 'http://www.snik.eu/ontology/ciox');

3. (Optional) Add virtual Triples
   1. Query `scripts/sparql/construct_virtual_triples_and_missing.sparql.txt` as N-Triples
   2. Upload the result to the graph `http://www.snik.eu/ontology/virtual`

## License
Because we extracted the triples from copyrighted books with permission of the publishers, we chose a noncommercial license with copyleft, the *Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International*, see LICENCE for details.
We want to encourage reuse, modification, derivation and distribution as much as possible, so if that license is a problem for you please contact [Prof. Winter](www.people.imise.uni-leipzig.de/alfred.winter) and we try our best to find a solution.
