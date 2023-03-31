from diagrams import Diagram, Cluster
from diagrams.aws.general import GenericDatabase

with Diagram("", direction="TB", filename="database_cluster", graph_attr={"bgcolor": "transparent", "pad": "0"}):
    with Cluster(""):
        db1 = GenericDatabase("")
        db2 = GenericDatabase("")
