from auth.client import init_client
from object.upload import upload_file
import argparse
import magic

parser = argparse.ArgumentParser()
parser.add_argument("-f","--file",help="Files which will be uploaded in the bucket",type=str,nargs="+")
parser.add_argument("-bn","--bucket_name",help="S3 Bucket name",type=str,nargs="?")


def main():
    s3_client = init_client()
    args = parser.parse_args()

    print(f"Uploading file(s) to \033[92m{args.bucket_name}\033[0m")
    
    for filename in args.file:
        m = magic.Magic(extension=True)
        try:
            extension = m.from_file(filename)
        except FileNotFoundError as e:
            print(f"{filename}: \033[91mFile not found\033[0m")
            continue

        if extension == "???":
            print(f"{filename}: \033[91mUnexpected extension\033[0m")
            continue

        if upload_file(s3_client, filename,args.bucket_name, extension):
            print(f"{filename}: \033[92mSuccess\033[0m")
        else:
            print(f"{filename}: \033[91mFail\033[0m")

main()