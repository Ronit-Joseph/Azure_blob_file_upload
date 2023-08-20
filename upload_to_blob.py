from azure.storage.blob import BlobServiceClient
import io

connection_string = "enter_connection_string"

blob_service_client = BlobServiceClient.from_connection_string(conn_str=connection_string)

container_name = "your_container_name"

container_client = blob_service_client.create_container(container_name)

blob_name = "name_of_blob"
#can adda for loop to continuously add multiple audio files in a folder
local_file_path = "path_to_local_audio_file"

with open(local_file_path, "rb") as data:
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(data, overwrite=True)
