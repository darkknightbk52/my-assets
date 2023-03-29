from diagrams import Cluster, Diagram
from diagrams.onprem.client import Client
from diagrams.generic.device import Mobile, Tablet

graph_attr = {
        "bgcolor": "transparent",
        "pad": "0",
}

with Diagram("", filename="clients", direction="TB", graph_attr=graph_attr):
    with Cluster(""):
        desktop = Client("")
        mobile = Mobile("")
        tablet = Tablet("")
