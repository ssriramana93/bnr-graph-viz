import pydot
import json

#class JSONFormatExtractor:
component_list = ["C1","C2","C3","C4"]
content_type_edge_color_map = {"ROSMSG": 'green', "JSON": 'blue'}


class GraphGenerator:
    def __init__(self, data):
        if not isinstance(data, dict):
            self.data = dict()
        else:
            self.data = data
        self.graph = pydot.Dot(graph_type='digraph')
        self.cluster = {}
        for component in component_list:
            self.cluster[component] = pydot.Cluster(graph_name=component, graph_type='digraph')
        self._update_graph()

    def _add_node_to_component(self,component_name,node):
        if (component_name not in self.cluster or not isinstance(node, pydot.Node)):
            return False
        self.cluster[component_name].add_node(node)
        return True

    def _update_graph(self):
        for cluster_name, cluster in self.cluster.iteritems():
            self.graph.add_subgraph(cluster)

    def _process_connection(self, connection):
        src = pydot.Node(connection["producer_process_name"])
        src_cluster = connection["producer_process_component"]
        self._add_node_to_component(src_cluster, src)
        dst = pydot.Node(connection["consumer_process_name"])
        dst_cluster = connection["consumer_process_component"]
        self._add_node_to_component(dst_cluster, dst)
        edge_attr = {}
        edge = pydot.Edge(src, dst)
        edge_attr['color'] = content_type_edge_color_map[connection['content_type']]
        edge = pydot.Edge(src, dst, color=content_type_edge_color_map[connection['content_type']])
        self.graph.add_edge(edge)


    def generate_graph(self):
        for connection in self.data["connections"]:
            self._process_connection(connection)


    def get_dot_file(self, path="result", file_format=".gif"):
        return self.graph.write(path, file_format)



with open('data.json', "r") as f:
  data = json.load(f)
graph_generator = GraphGenerator(data)
graph_generator.generate_graph()
print graph_generator.get_dot_file()
