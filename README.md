# Custom CLI Script for Uploading files in S3 Bucket

script can be used to upload files to amazon s3 bucket in the corresponding folder of the extension. For example:
test.pdf file will be uploaded in pdf/ folder

### Note

- Script is written in _Python3_
- install requirements using the command below:

  `pip3 install -r requirements.txt`
  OR
  `poetry install`

Example with poetry:
`poetry run python main.py -bn YOUR_BUCKET_NAME -f FILENAME1 FILENAME2`

Example without poetry
`python3 main.py -bn YOUR_BUCKET_NAME -f FILENAME1 FILENAME2`
