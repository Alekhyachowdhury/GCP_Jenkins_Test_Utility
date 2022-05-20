import os
import json
import sys
import base64
from google.cloud import pubsub_v1
from google.api_core import retry
from concurrent import futures

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="key.json"

def write_payload(payload,payload_name):
    try:
        payload_file = open(payload_name,mode="w",encoding="utf-8")
        payload_file.write(payload)
        payload_file.close()
        return "Succes"
    except Exception as e:
        print(e)
        return "Failure"


print("#### In PubSub_Listener ####")
print("#### Project_Id:" + sys.argv[1] + " ####")
Project_Id = sys.argv[1]
print("#### Subscription_Id:" + sys.argv[2] + " ####")
Subscription_Id = sys.argv[2]
print("#### Payload_Name:" + sys.argv[3] + " ####")
Payload_Name = sys.argv[3]

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(Project_Id, Subscription_Id)

NUM_MESSAGES = 1

# Wrap the subscriber in a 'with' block to automatically call close() to
# close the underlying gRPC channel when done.
with subscriber:
    # The subscriber pulls a specific number of messages. The actual
    # number of messages pulled may be smaller than max_messages.
    response = subscriber.pull(request={"subscription": subscription_path, "max_messages": NUM_MESSAGES},retry=retry.Retry(deadline=300),)
    
    #if len(response.received_messages) == 0:
    #    return

    ack_ids = []
    for received_message in response.received_messages:
        #print(f"Received: {received_message.message.data}.")
        print("#### pubsub message id ####")
        print(received_message.message.message_id)
        
        ack_ids.append(received_message.ack_id)
        write_payload(json.dumps(received_message.message.data.decode("utf-8")),Payload_Name)
        
    # Acknowledges the received messages so they will not be sent again.

    
    subscriber.acknowledge(request={"subscription": subscription_path, "ack_ids": ack_ids})
       
    




