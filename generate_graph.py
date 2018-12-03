import pydot
import json

#class JSONFormatExtractor:


class GraphGenerator:
    def __init__(self, data):
        if not isinstance(data, dict):
            self.data = dict()
        else:
            self.data = data
        self.graph = pydot.Dot(graph_type='digraph')

    def generate_graph(self):
        for connection in self.data["connections"]:
            src = pydot.Node(connection["producer_process_name"])
            dst = pydot.Node(connection["consumer_process_name"])
            edge = pydot.Edge(src, dst)
            self.graph.add_edge(edge)

    def get_dot_file(self, path="data", file_format=".gif"):
        return self.graph.write(path, file_format)



with open('data.json', "r") as f:
  data = json.load(f)
print data
print data["connections"]
graph_generator = GraphGenerator(data)
graph_generator.generate_graph()
print graph_generator.get_dot_file()
