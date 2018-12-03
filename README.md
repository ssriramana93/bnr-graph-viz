# bnr-graph-viz

This is a model system for generating the graph from JSON data.
The `generate_json.py` script contains some dummy JSON data.
The data contains nodes clustered into components and there are connections between 
these nodes either within the component or accross components.

The `generate_graph.py` script contains the `GraphGenerator` class which acts as the interface between 
`pydot` and the `data.json` file and helps generate the `.dot` file.


The resulting diagram is in `result`
