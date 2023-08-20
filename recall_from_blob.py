from azure.storage.blob import BlobServiceClient
import io


connection_string = "enter_connection_string"

blob_service_client = BlobServiceClient.from_connection_string(conn_str=connection_string)


container_name = "enter_container_name"

container_client = blob_service_client.get_container_client(container_name)

blob_name = "name_of_blob"

blob_client = container_client.get_blob_client(blob_name)
audio_data = blob_client.download_blob().readall()


