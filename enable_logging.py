import logging
import sys
from azure.storage.blob import BlobClient
from azure.identity import DefaultAzureCredential

# Set the logging level for all azure-storage-* libraries
logger = logging.getLogger('azure.storage')
logger.setLevel(logging.INFO)

# Set the logging level for all azure-* libraries
logger = logging.getLogger('azure')
logger.setLevel(logging.ERROR)

# Direct logging output to stdout. Without adding a handler,
# no logging output is captured.
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)

# endpoint is the Blob storage URL.
endpoint = 'azuerml4140135745.blob.core.windows.net/azureml-blobstore-283c646f-cf59-416d-8fe7-d0db144034ca'
client = BlobClient(endpoint, DefaultAzureCredential(), logging_enable=True, blob_name='workspaceblobstore')

print(f"Logger enabled for INFO={logger.isEnabledFor(logging.INFO)}, " \
    f"WARNING={logger.isEnabledFor(logging.WARNING)}, " \
    f"INFO={logger.isEnabledFor(logging.INFO)}, " \
    f"DEBUG={logger.isEnabledFor(logging.DEBUG)}")