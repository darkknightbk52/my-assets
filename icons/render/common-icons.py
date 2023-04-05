from diagrams import Diagram, Edge
from diagrams.c4 import Container
from diagrams.programming.flowchart import Decision
from diagrams.onprem.inmemory import Redis
from diagrams.digitalocean.compute import Droplet
from diagrams.aws.network import ElbNetworkLoadBalancer
from diagrams.aws.general import Client, MobileClient
from diagrams.aws.database import ElasticacheCacheNode
from diagrams.aws.general import GenericDatabase, TraditionalServer
from diagrams.custom import Custom
import os
from urllib.request import urlretrieve
from diagrams.azure.network import CDNProfiles, DNSZones
from diagrams.gcp.operations import Monitoring
from diagrams.firebase.grow import Messaging
from diagrams.saas.communication import Twilio
from diagrams.azure.integration import SendgridAccounts
from diagrams.aws.migration import ApplicationDiscoveryService
from diagrams.aws.general import User
from diagrams.aws.security import WAFFilteringRule
from diagrams.aws.iot import IotFireTv
from diagrams.aws.storage import SimpleStorageServiceS3BucketWithObjects
from diagrams.generic.device import Tablet
from diagrams.aws.storage import S3Glacier

def icon(name):
    name = name + ".png"
    asset_url = "https://raw.githubusercontent.com/darkknightbk52/my-assets/main/icons/" + name
    icon_dir = "/tmp/icons/"
    icon_path = icon_dir + name
    if (not os.path.isdir(icon_dir)):
        os.makedirs(icon_dir, 0o777)
    if (not os.path.isfile(icon_path)):
        urlretrieve(asset_url, icon_path)
    return icon_path
with Diagram("Common Icons", graph_attr={"linelength": "256"}) as dot:
    edge = Edge(label="                  ")

    container = Container("Container", description="c4.container.Container")
    decision = Decision("programming.flowchart.Decision")
    redis = Redis("onprem.inmemory.Redis")
    droplet = Droplet("digitalocean.compute.Droplet")
    load_balancer = ElbNetworkLoadBalancer("aws.network.ElbNetworkLoadBalancer")

    desktop = Client("aws.general.Client")
    mobile = MobileClient("aws.general.MobileClient")
    cache = ElasticacheCacheNode("aws.database.ElasticacheCacheNode")
    database = GenericDatabase("aws.general.GenericDatabase") 
    server = TraditionalServer("aws.general.TraditionalServer")

    clients = Custom("clients.png", icon("clients"))
    message_queue = Custom("message_queue.png", icon("message_queue"))
    server_cluster = Custom("server_cluster.png", icon("server_cluster"))
    cache_cluster = Custom("cache_cluster.png", icon("cache_cluster"))
    database_cluster = Custom("database_cluster.png", icon("database_cluster"))

    dns_resolver = DNSZones("azure.network.DNSZones")
    monitoring = Monitoring("gcp.operations.Monitoring")
    apns = Custom("ios_apns.png", icon("ios_apns"))
    fcm = Messaging("firebase.grow.Messaging")
    twilio = Twilio("saas.communication.Twilio")
    sendgrid = SendgridAccounts("azure.integration.SendgridAccounts")
    graph_db = Custom("graph_db.png", icon("graph_db"))
    cdn = CDNProfiles("azure.network.CDNProfiles")
    user = User("aws.general.User")
    service_discovery = ApplicationDiscoveryService("aws.migration.ApplicationDiscoveryService")
    filter = WAFFilteringRule("aws.security.WAFFilteringRule")
    log_file = Custom("log_file.png", icon("log_file"))
    tv = IotFireTv("aws.iot.IotFireTv")
    s3 = SimpleStorageServiceS3BucketWithObjects("aws.storage.SimpleStorageServiceS3BucketWithObjects")
    tablet = Tablet("generic.device.Tablet")
    notifications = Custom("notifications.png", icon("notifications"))
    s3_glacier = S3Glacier("aws.storage.S3Glacier")

    container >> edge >> decision >> edge >> redis >> edge >> droplet >> edge >> desktop >> edge >> mobile >> edge >> cache >> edge >> database
    clients >> edge >> message_queue >> edge >> server_cluster >> edge >> cache_cluster >> edge >> database_cluster >> edge >> load_balancer >> server
    dns_resolver >> edge >> monitoring >> apns >> fcm >> twilio >> sendgrid >> graph_db >> cdn
    user >> filter >> log_file >> tv >> tablet >> notifications >> s3_glacier
    service_discovery >> Edge(minlen="2") >> s3
