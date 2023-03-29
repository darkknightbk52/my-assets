from diagrams import Cluster, Diagram
from diagrams.onprem.compute import Server

graph_attr = {
        "bgcolor": "transparent",
        "pad": "0",
}

with Diagram("", filename="server_cluster", direction="TB", graph_attr=graph_attr, show=False):
    with Cluster(""):
        server1 = Server("")
        server2 = Server("")
