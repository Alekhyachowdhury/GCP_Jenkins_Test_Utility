
import os
import json
import sys
from google.cloud import storage



def read_json_payload(payload_name):
    try:
        with open(payload_name,mode="r",encoding="utf-8") as input_file:            
            data = json.load(input_file)            
            return data
    except Exception as e:
        print(e)
        return "Failure"


print("#### In Verify Payload ####")
print("#### Project_Id:" + sys.argv[1] + " ####")
Project_Id = sys.argv[1]
print("#### Topic_Name:" + sys.argv[2] + " ####")
Expected_Response = sys.argv[2]
print("#### Payload_Name:" + sys.argv[3] + " ####")
Actual_Response = sys.argv[3]

expected_response_content = read_json_payload(Expected_Response)
print("#### expected_response_content ####")
print(expected_response_content)
actual_response_content = read_json_payload(Actual_Response)
print("#### actual_response_content ####")
print(actual_response_content)
if (expected_response_content == actual_response_content):
    print("#### Successful Validation ####")
else:
    print("#### Validation Failure ####")

