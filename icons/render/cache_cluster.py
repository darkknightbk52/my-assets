from diagrams import Diagram, Cluster
from diagrams.aws.database import ElasticacheCacheNode

with Diagram("", direction="TB", filename="cache_cluster", graph_attr={"bgcolor": "transparent", "pad": "0"}):
    with Cluster(""):
        cache1 = ElasticacheCacheNode("")
        cache2 = ElasticacheCacheNode("")
