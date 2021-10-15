## Warning
This is the old storage location of the SNIK ontology RDF dump. The official SPARQL Endpoint http://www.snik.eu/sparql contains the current version, which is shown in the graph visualization http://www.snik.eu/graph. Changes to these files here will not influence the contents of the SPARQL endpoint, use the OntoWiki at http://www.snik.eu/ontowiki for that.

To generate an up-to-date dump of a subontology, enter `DESCRIBE <http://www.snik.eu/ontology/`*subontology*`>` into the [SPARQL endpoint](http://www.snik.eu/sparql), for example [`DESCRIBE <http://www.snik.eu/ontology/bb>`](http://www.snik.eu/sparql?default-graph-uri=&query=DESCRIBE+%3Chttp%3A%2F%2Fwww.snik.eu%2Fontology%2Fbb%3E&should-sponge=&format=application%2Frdf%2Bxml&timeout=0&debug=on).

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
    
    xmllint --noout filename.rdf
    rapper -i rdfxml -c filename.rdf

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

    DB.DBA.RDF_GRAPH_GROUP_INS ('http://www.snik.eu/ontology', 'http://www.snik.eu/ontology/bb');
    DB.DBA.RDF_GRAPH_GROUP_INS ('http://www.snik.eu/ontology', 'http://www.snik.eu/ontology/ob');
    DB.DBA.RDF_GRAPH_GROUP_INS ('http://www.snik.eu/ontology', 'http://www.snik.eu/ontology/meta');
    DB.DBA.RDF_GRAPH_GROUP_INS ('http://www.snik.eu/ontology', 'http://www.snik.eu/ontology/ciox');

3. (Optional) Add virtual Triples
   1. Query `sparql/construct_virtual_triples_and_missing.sparql.txt` as N-Triples
   2. Upload the result to the graph `http://www.snik.eu/ontology/virtual`

## Updating from SPARQL endpoint---Outdated
The source of truth for most files used to be the SPARQL endpoint, but this repository is still regularily updated in the following manner.
Exceptions are match.nt, limes-exact.nt and persian.nt, whose source of truth has always been the repository.

### Save SPARQL dump on the server
Replace YYYYMMDD with the current date.

    dump_one_graph ('http://www.snik.eu/ontology/meta', './dumps/YYYYMMDDmeta', 1000000000);
    dump_one_graph ('http://www.snik.eu/ontology/he', './dumps/YYYYMMDDhe', 1000000000);
    dump_one_graph ('http://www.snik.eu/ontology/he-unconsolidated', './dumps/YYYYMMDDhe-unconsolidated', 1000000000);
    dump_one_graph ('http://www.snik.eu/ontology/bb', './dumps/YYYYMMDDbb', 1000000000);
    dump_one_graph ('http://www.snik.eu/ontology/ob', './dumps/YYYYMMDDob', 1000000000); 
    dump_one_graph ('http://www.snik.eu/ontology/ciox', './dumps/YYYYMMDDciox', 1000000000); 
    dump_one_graph ('http://www.snik.eu/ontology/it', './dumps/YYYYMMDDit', 1000000000); 
    dump_one_graph ('http://www.snik.eu/ontology/it4it', './dumps/YYYYMMDDit4it', 1000000000); 

### Download SPARQL dump from the server
1. Change directory to your dump folder and run `scp -r "root@bruchtal:/var/lib/docker/volumes/sniktoolset_virtuoso-data/_data/dumps/YYYYMMDD*" .`
2. Use [virtuoso2git](https://github.com/KonradHoeffner/virtuoso2git) to overwrite the source files in your repository, e.g. `dumps$ virtuoso2git . ~/projekte/snik/ontology 20201117`
3. Merge he.nt and he-unconsolidated.nt

```
$ cat he.nt he-unconsolidated.nt| LC_ALL=en_US.UTF-8 sort | uniq | less > /tmp/he.nt
$ mv /tmp/he.nt .
```

### Inspect, commit and push
Use vimdiff to check for irregularites, such as massive diffs due to differences in sort order or blank node renamings. If everything is OK, commit and push as normal.


## License
Because we extracted the triples from copyrighted books with permission of the publishers, we chose a noncommercial license with copyleft, the *Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International*, see LICENCE for details.
We want to encourage reuse, modification, derivation and distribution as much as possible, so if that license is a problem for you please contact [Prof. Winter](www.people.imise.uni-leipzig.de/alfred.winter) and we try our best to find a solution.
