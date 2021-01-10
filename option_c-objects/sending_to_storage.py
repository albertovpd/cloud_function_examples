
from google.cloud import storage

# Read the README. Option C.

def upload_blob(source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    bucket_name = "--yourbucketname--"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

print("UPLOADING PICS")
upload_blob("../tmp/RFE_columns.png","RFE_columns.png")
upload_blob("../tmp/outliers.png","outliers.png")
print("PICS SENT")