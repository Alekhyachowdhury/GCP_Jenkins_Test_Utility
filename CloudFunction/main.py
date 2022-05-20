import base64
import json
from google.cloud import pubsub_v1

def mapper(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')

    received_json = json.loads(pubsub_message)

    processed_json = {}

    processed_json["ItemType"] = received_json["item_type"]
    processed_json["ItemQty"] = received_json["quantity"]

    processed_str = json.dumps(processed_json)

    publisher = pubsub_v1.PublisherClient()

    topic_path = publisher.topic_path("gcp_project_name", "output_pubsub_topic")

    publish_future = publisher.publish(topic_path, processed_str.encode("utf-8"))
    
    result = publish_future.result()  

    print(pubsub_message)
