
import os
import json
import sys
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="key.json"

def write_payload(json_payload,payload_name):
    try:
        payload_file = open(payload_name,mode="w",encoding="utf-8")
        payload = json.dumps(json_payload)
        payload_file.write(payload)
        payload_file.close()
        return "Succes"
    except Exception as e:
        print(e)
        return "Failure"



print("#### In Get_Payload ####")
print("#### Project_Id:" + sys.argv[1] + " ####")
Project_Id = sys.argv[1]
print("#### Bucket_Name:" + sys.argv[2] + " ####")
Bucket_Name = sys.argv[2]
print("#### Folder_Name:" + sys.argv[3] + " ####")
Folder_Name = sys.argv[3]
print("#### Payload_Name:" + sys.argv[4] + " ####")
Payload_Name = sys.argv[4]

Payload_path = Folder_Name +  "/" + Payload_Name
print("#### Payload_Name:" + Payload_path + " ####")

client = storage.Client(project=Project_Id)
bucket = client.get_bucket(Bucket_Name)
blob = bucket.get_blob(Payload_path)
json_obj = json.loads(blob.download_as_string())
write_payload(json_obj,Payload_Name)





