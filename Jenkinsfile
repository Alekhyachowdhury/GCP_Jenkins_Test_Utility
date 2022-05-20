import hudson.model.*

node {

    stage('Install dependecies') {
         sh """
         pwd
         pip3.10 install google-cloud-pubsub
         pip3.10 install google-cloud-storage
         pip3.10 install google-api-core
         pip3.10 install google-cloud-bigquery
         pip3.10 install pybase64
         """        
    }

    stage('Git clone') {
         sh """
         pwd
         rm -rf GCP_Jenkins_Test_Utility
         git clone https://username:personal_access_topken@github.com/repository_url.git -b branch                
         """        
    }

    stage('Get Input payload from GCS') {
         sh """
         pwd
         cd GCP_Jenkins_Test_Utility
         python3.10 Get_Payload.py gcp_project_name payload_repository gcs_folder input.json
         """        
    }

    stage('Get Expected Output payload from GCS') {
         sh """
         pwd
         cd GCP_Jenkins_Test_Utility
         python3.10 Get_Payload.py gcp_project_name payload_repository gcs_folder expected_output.json
         """        
    }

    stage('Verify Payloads') {
         sh """
         pwd
         cd GCP_Jenkins_Test_Utility
         ls -l
         """
        
    }

    stage('Publish to PubSub') {
         sh """
         pwd
         cd GCP_Jenkins_Test_Utility
         python3.10 PubSub_Publisher.py gcp_project_name input_pubsub_topic input.json
         ls -l
         echo "#### pubsub message id ####"
         cat pubsub_ack.txt
         """        
    }

    stage('Listen to PubSub') {
         sh """
         pwd
         cd GCP_Jenkins_Test_Utility
         python3.10 PubSub_Listener.py gcp_project_name output_pubsub_topic-sub received_payload.json
         ls -l         
         """        
    }

    stage('Compare Payloads') {
         sh """
         pwd
         cd GCP_Jenkins_Test_Utility
         python3.10 Verify_Payload.py gcp_project_name expected_output.json received_payload.json         
         """        
    }

}
