from diagrams import Cluster, Diagram
from diagrams.aws.general import Client, MobileClient

graph_attr = {
        "bgcolor": "transparent",
        "pad": "0",
}

with Diagram("", filename="clients", direction="TB", graph_attr=graph_attr):
    with Cluster(""):
        desktop = Client("")
        mobile = MobileClient("")
