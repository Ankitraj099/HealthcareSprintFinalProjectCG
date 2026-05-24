from azure.storage.blob import BlobServiceClient
import pandas as pd
import io
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Azure configuration
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = os.getenv("AZURE_CONTAINER_NAME")

# Create blob service client
blob_service_client = BlobServiceClient.from_connection_string(
    connection_string
)

def upload_prediction_to_blob(prediction_data):

    blob_name = "live_predictions.csv"

    # Get blob client
    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=blob_name
    )

    # Convert new prediction to dataframe
    new_df = pd.DataFrame([prediction_data])

    try:
        # Download existing blob
        download_stream = blob_client.download_blob()

        existing_csv = download_stream.readall()

        # Read existing CSV
        existing_df = pd.read_csv(
            io.BytesIO(existing_csv)
        )

        # Append new prediction
        updated_df = pd.concat(
            [existing_df, new_df],
            ignore_index=True
        )

        print("Existing CSV found. Appending data...")

    except Exception as e:

        # If blob doesn't exist yet
        updated_df = new_df

        print("New CSV file created.")

    # Convert dataframe to CSV
    csv_buffer = io.StringIO()

    updated_df.to_csv(
        csv_buffer,
        index=False
    )

    # Upload updated CSV to Azure Blob
    blob_client.upload_blob(
        csv_buffer.getvalue(),
        overwrite=True
    )

    print("Prediction appended successfully to Azure Blob Storage")