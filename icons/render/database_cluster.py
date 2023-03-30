from diagrams import Diagram, Cluster
from diagrams.aws.database import Database

with Diagram("", direction="TB", filename="database_cluster", graph_attr={"bgcolor": "transparent", "pad": "0"}):
    with Cluster(""):
        db1 = Database("")
        db2 = Database("")
