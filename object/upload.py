import logging
from pathlib import Path
from botocore.exceptions import ClientError

def upload_file(s3client,filename,bucketname, folder_path):
    try:
        s3client.upload_file(filename, bucketname, f"{folder_path}/{filename}")
        return True
    except ClientError as e:
        logging.error(e)
    except FileNotFoundError as e:
        return False
    return False