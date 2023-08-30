<img align="right" width="200" height="200" src="https://avatars.githubusercontent.com/u/79194034?s=400&u=6f1a8e449234d0daa440de87a64f718a9c804593&v=4" alt="SNIK">

# SNIK Ontology

[![build](https://github.com/snikproject/ontology/actions/workflows/build.yml/badge.svg)](https://github.com/snikproject/ontology/actions/workflows/build.yml)
[![SHACL status](https://github.com/snikproject/ontology/actions/workflows/shacl.yml/badge.svg)](https://github.com/snikproject/ontology/actions/workflows/shacl.yml)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-blue.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![DOI](https://zenodo.org/badge/65827715.svg)](https://zenodo.org/badge/latestdoi/65827715)

SNIK is an ontology of information management in hospitals that consists of a meta model and several subontologies.

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

## Setup your own SPARQL Endpoint

### KBox
For testing you can setup a local SPARQL endpoint with a single command using KBox, which you can install using `pip install kbox` or using docker, which we show here:

```
docker run -p 8080:8080 aksw/kbox:v0.0.2-alpha -server -kb "http://www.snik.eu/ontology" -install
```

Ignore the message and open `http://localhost:8080/` in a browser.

### Existing Virtuoso SPARQL Endpoint

#### All in one Graph
Run `scripts/combine` to merge everything into one file `/tmp/snik.ttl`, which you can upload to the graph `http://www.snik.eu/ontology`.

#### Graph Group and Subgraphs
1. Go to “Linked Data”->"Quad Store Upload” and upload the files.

File		| Graph
--			| --
meta.ttl	|http://www.snik.eu/ontology/meta
bb.ttl		|http://www.snik.eu/ontology/bb
ob.ttl		|http://www.snik.eu/ontology/ob
ciox.ttl	|http://www.snik.eu/ontology/ciox
it4it.ttl	|http://www.snik.eu/ontology/it4it
limes.nt	|http://www.snik.eu/ontology/limes-exact
match.nt	|http://www.snik.eu/ontology/match

Check if it worked by querying `SELECT COUNT(*) ?graph {GRAPH ?graph {?s ?p ?o.}} ORDER BY DESC(COUNT(*))`.

2. Add graphs to the graph group in the Virtuoso Conductor ISQL panel and create the namespaces

		DB.DBA.RDF_GRAPH_GROUP_CREATE('http://www.snik.eu/ontology',1);
		DB.DBA.RDF_GRAPH_GROUP_INS ('http://www.snik.eu/ontology', 'http://www.snik.eu/ontology/bb');
		DB.DBA.RDF_GRAPH_GROUP_INS ('http://www.snik.eu/ontology', 'http://www.snik.eu/ontology/ob');
		DB.DBA.RDF_GRAPH_GROUP_INS ('http://www.snik.eu/ontology', 'http://www.snik.eu/ontology/meta');
		DB.DBA.RDF_GRAPH_GROUP_INS ('http://www.snik.eu/ontology', 'http://www.snik.eu/ontology/ciox');
		DB.DBA.RDF_GRAPH_GROUP_INS ('http://www.snik.eu/ontology', 'http://www.snik.eu/ontology/it4it');
		DB.DBA.RDF_GRAPH_GROUP_INS ('http://www.snik.eu/ontology', 'http://www.snik.eu/ontology/he');
		DB.DBA.XML_SET_NS_DECL ('sniko', 'http://www.snik.eu/ontology/', 2);                
		DB.DBA.XML_SET_NS_DECL ('meta', 'http://www.snik.eu/ontology/meta/', 2);
		DB.DBA.XML_SET_NS_DECL ('bb', 'http://www.snik.eu/ontology/bb/', 2);
		DB.DBA.XML_SET_NS_DECL ('ob', 'http://www.snik.eu/ontology/ob/', 2);
		DB.DBA.XML_SET_NS_DECL ('he', 'http://www.snik.eu/ontology/he/', 2);
		DB.DBA.XML_SET_NS_DECL ('ciox', 'http://www.snik.eu/ontology/ciox/', 2);
		DB.DBA.XML_SET_NS_DECL ('it4it', 'http://www.snik.eu/ontology/it4it/', 2);

3. (Optional) Add virtual Triples
   1. Query `scripts/sparql/construct_virtual_triples_and_missing.sparql.txt` as N-Triples
   2. Upload the result to the graph `http://www.snik.eu/ontology/virtual`

## Editing for Project Members

* Edit only with a text editor.
* Please make sure that you produce the smallest diff possible for your changes, e.g. don't use a tool that shuffles the definition locations around or changes line endings or indentation.
* Verify after editing with:
    
    rapper -i turtle -c filename.ttl

## SHACL
SHACL shapes for closed-world validation are included in `shacl.ttl`.
Validate with `scripts/shacl`.

## Docker
The [docker compose setup](https://github.com/snikproject/docker) includes a Virtuoso SPARQL endpoint preloaded with the different SNIK graphs and namespaces, an [RDF Browser](https://github.com/snikproject/lodview) and more.

## License
Because we extracted the triples from copyrighted books with permission of the publishers, we chose a noncommercial license with copyleft, the *Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International*, see LICENCE for details.
The tools developed in the SNIK project have the same license for simplicity's sake and there was never a reason to change it.
However we want to encourage reuse, modification, derivation and distribution as much as possible, so if that license is a problem for you please contact [Prof. Winter](www.people.imise.uni-leipzig.de/alfred.winter) and we try our best to find a solution.
