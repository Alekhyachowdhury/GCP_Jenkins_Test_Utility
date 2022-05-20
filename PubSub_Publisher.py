import os
from google.cloud import pubsub_v1
from concurrent import futures
import json
import sys

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="key.json"


def read_json_payload(payload_name):
    try:
        with open(payload_name,mode="r",encoding="utf-8") as input_file:            
            data = json.load(input_file)            
            return data
    except Exception as e:
        print(e)
        return "Failure"

def write_payload(payload,payload_name):
    try:
        payload_file = open(payload_name,mode="w",encoding="utf-8")
        payload_file.write(payload)
        payload_file.close()
        return "Succes"
    except Exception as e:
        print(e)
        return "Failure"



print("#### In PubSub_Publisher ####")
print("#### Project_Id:" + sys.argv[1] + " ####")
Project_Id = sys.argv[1]
print("#### Topic_Name:" + sys.argv[2] + " ####")
Topic_Name = sys.argv[2]
print("#### Payload_Name:" + sys.argv[3] + " ####")
Payload_Name = sys.argv[3]


json_input_payload = read_json_payload(Payload_Name)
print(json_input_payload)
publish_payload = json.dumps(json_input_payload)

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(Project_Id, Topic_Name)
publish_future = publisher.publish(topic_path, publish_payload.encode("utf-8"))
result = publish_future.result()
write_payload(result,"pubsub_ack.txt")


